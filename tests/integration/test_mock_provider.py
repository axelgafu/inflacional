from tests.mocks.provider import MockSIEProvider
import pytest
import os

def test_mock_provider_loads_json():
    """
    Verifies that MockSIEProvider loads data from the correct JSON file.
    """
    provider = MockSIEProvider()
    data = provider.get_series_data("SP1")
    
    assert "bmx" in data
    assert data["bmx"]["series"][0]["idSerie"] == "SP1"
    assert len(data["bmx"]["series"][0]["datos"]) == 2

def test_mock_provider_raises_error_if_missing():
    """
    Verifies that MockSIEProvider raises FileNotFoundError if mock file doesn't exist.
    """
    provider = MockSIEProvider()
    with pytest.raises(FileNotFoundError):
        provider.get_series_data("NON_EXISTENT")
