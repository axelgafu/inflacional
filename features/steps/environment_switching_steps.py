from behave import given, when, then
import os
from src.banxico_report.api.factory import SIEProviderFactory
from src.banxico_report.api.real import RealSIEProvider
# We import MockSIEProvider from tests/mocks/provider
from tests.mocks.provider import MockSIEProvider

@given('the environment variable "{var_name}" is not set')
def step_impl(context, var_name):
    if var_name in os.environ:
        del os.environ[var_name]

@given('the environment variable "{var_name}" is set to "{value}"')
def step_impl(context, var_name, value):
    os.environ[var_name] = value

@when('I request the API provider')
def step_impl(context):
    try:
        context.provider = SIEProviderFactory.get_provider()
    except Exception as e:
        context.exception = e

@then('the provider should be an instance of "{class_name}"')
def step_impl(context, class_name):
    if class_name == "RealSIEProvider":
        assert isinstance(context.provider, RealSIEProvider)
    elif class_name == "MockSIEProvider":
        assert isinstance(context.provider, MockSIEProvider)
    else:
        raise ValueError(f"Unknown class name: {class_name}")
