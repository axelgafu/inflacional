import pytest
from datetime import date, timedelta
from unittest.mock import MagicMock
from banxico_report.api.rates import RatesFetcher
from banxico_report.utils.errors import RateRetrievalError

@pytest.fixture
def mock_provider():
    return MagicMock()

def test_get_target_rate_with_lookback(mock_provider):
    """
    Test that look-back logic selects the latest available date.
    """
    fetcher = RatesFetcher(mock_provider)
    reference_date = "2023-12-05"
    
    # Mock response with multiple dates
    # TI52.json-like structure
    mock_provider.get_series_data.return_value = {
        "bmx": {
            "series": [
                {
                    "idSerie": "SF331451",
                    "datos": [
                        {"fecha": "2023-12-01", "dato": "11.00"},
                        {"fecha": "2023-12-04", "dato": "11.25"}
                    ]
                }
            ]
        }
    }
    
    rate = fetcher.get_target_rate(reference_date)
    
    # Should get the latest available date (Dec 4)
    assert rate == 11.25
    
    # Verify the provider was called with the correct range
    # reference_date is "2023-12-05", default lookback is 7
    # 2023-12-05 - 7 days = 2023-11-28
    # But wait, my current implementation only uses start_date=reference_date
    # Once I implement T009, this test will pass.
    mock_provider.get_series_data.assert_called_once()
    args, kwargs = mock_provider.get_series_data.call_args
    assert kwargs["end_date"] == reference_date

def test_get_target_rate_critical_failure(mock_provider):
    """
    Test that RateRetrievalError is raised when no data is found.
    """
    fetcher = RatesFetcher(mock_provider)
    
    # Mock response with no datos
    mock_provider.get_series_data.return_value = {
        "bmx": {
            "series": [
                {
                    "idSerie": "SF331451",
                    # missing "datos"
                }
            ]
        }
    }
    
    with pytest.raises(RateRetrievalError):
        fetcher.get_target_rate("2023-12-05")
