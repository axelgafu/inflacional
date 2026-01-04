import pytest
import os
from src.banxico_report.api.rates import RatesFetcher
from src.banxico_report.api.factory import SIEProviderFactory

def test_get_target_rate_mock(monkeypatch):
    """
    Integration test using the MockSIEProvider through the factory.
    """
    monkeypatch.setenv("INFLACIONAL_ENV", "test")
    
    # We use the factory to get the provider (which should be MockSIEProvider)
    provider = SIEProviderFactory.get_provider()
    fetcher = RatesFetcher(provider)
    
    # This date should be in the TI52.json mock file
    # We use a date that is in our mock file created in the BDD step
    rate = fetcher.get_target_rate("2023-12-01")
    
    # Currently it will return 10.25 (hardcoded)
    # After refactor it should return 11.25 (from mock)
    assert rate == 11.25
