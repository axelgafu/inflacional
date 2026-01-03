import pytest
from unittest.mock import MagicMock
from banxico_report.api.rates import RatesFetcher
from banxico_report.api.exchange import ExchangeRateFetcher

def test_rates_fetcher():
    client = MagicMock()
    fetcher = RatesFetcher(client)
    rate = fetcher.get_target_rate(None)
    assert rate == 10.25

def test_exchange_rate_fetcher():
    client = MagicMock()
    fetcher = ExchangeRateFetcher(client)
    variation = fetcher.get_fix_variation(None)
    assert variation == 0.05
