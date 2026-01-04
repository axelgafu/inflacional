from behave import given, when, then
import os
import json
from src.banxico_report.api.rates import RatesFetcher
from tests.mocks.provider import MockSIEProvider

@given('the application is in test mode')
def step_impl(context):
    os.environ["INFLACIONAL_ENV"] = "test"
    # Ensure provider is fresh
    context.provider = MockSIEProvider()

@given('mock data for series "{serie_id}" exists with value "{value}" for date "{date_str}"')
def step_impl(context, serie_id, value, date_str):
    # This ensures the mock file is present with the expected data
    # (T001 already ensures TI52 exists, but we can verify/overwrite if needed)
    mock_dir = os.path.join("tests", "mocks", "sie")
    os.makedirs(mock_dir, exist_ok=True)
    file_path = os.path.join(mock_dir, f"{serie_id}.json")
    
    mock_data = {
        "bmx": {
            "series": [
                {
                    "idSerie": serie_id,
                    "datos": [{"fecha": date_str, "dato": value}]
                }
            ]
        }
    }
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(mock_data, f)

@when('I fetch the target rate for "{date_str}"')
def step_impl(context, date_str):
    fetcher = RatesFetcher(context.provider)
    try:
        context.result = fetcher.get_target_rate(date_str)
    except Exception as e:
        context.exception = e

@then('the result should be "{expected_value}"')
def step_impl(context, expected_value):
    assert str(context.result) == expected_value
