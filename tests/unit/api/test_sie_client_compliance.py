import pytest
from unittest.mock import MagicMock, patch
from banxico_report.api.sie_client import SIEClient

@pytest.fixture
def client():
    return SIEClient(token="testing-token")

@patch("banxico_report.api.sie_client.requests.get")
def test_header_authentication_enforced(mock_get, client):
    """
    FR-001: The SIEClient MUST send the API token using the Bmx-Token HTTP header.
    FR-002: The SIEClient MUST NOT use query parameters for authentication.
    """
    series_id = "SF43718"
    client.get_series_data(series_id)
    
    # Check that requests.get was called
    mock_get.assert_called_once()
    
    args, kwargs = mock_get.call_args
    headers = kwargs.get("headers", {})
    
    # 1. Header must be present and correct
    assert "Bmx-Token" in headers, "Bmx-Token header missing"
    assert headers["Bmx-Token"] == "testing-token"
    
    # 2. URL should NOT contain token query param
    url = args[0]
    assert "token=" not in url, "Token found in URL query parameters (should be in header only)"

@patch("banxico_report.api.sie_client.requests.get")
def test_date_format_compliance(mock_get, client):
    """
    FR-003: API requests MUST use YYYY-MM-DD date format in URL path.
    """
    series_id = "SF43718"
    # Provide dates in potentially different formats or datetime objects
    # Ideally the client should handle conversion, but ensuring strict format usage
    start_date = "2023-01-01"
    end_date = "2023-01-31"
    
    client.get_series_data(series_id, start_date=start_date, end_date=end_date)
    
    args, _ = mock_get.call_args
    url = args[0]
    
    expected_segment = "/2023-01-01/2023-01-31"
    assert expected_segment in url, f"URL {url} does not contain expected date segment {expected_segment}"

def test_invalid_date_format_raises_error(client):
    """
    FR-003: Client should raise ValueError if dates are not YYYY-MM-DD.
    """
    series_id = "SF43718"
    # Invalid format DD-MM-YYYY
    with pytest.raises(ValueError, match="Date must be in YYYY-MM-DD format"):
        client.get_series_data(series_id, start_date="01-01-2023", end_date="31-01-2023")
