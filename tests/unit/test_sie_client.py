import pytest
import requests
from unittest.mock import MagicMock, patch
from banxico_report.api.sie_client import SIEClient

def test_sie_client_success():
    tracker = MagicMock()
    client = SIEClient(token="test", tracker=tracker)
    
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "ok"}
        mock_get.return_value = mock_response
        
        result = client.get_series_data("SERIE1", "2026-01-01", "2026-01-02")
        
        assert result == {"data": "ok"}
        tracker.record_call.assert_called_once()
        mock_get.assert_called_once()

def test_sie_client_429():
    client = SIEClient(token="test")
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 429
        # raise_for_status throws HTTPError
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()
        mock_get.return_value = mock_response
        
        with pytest.raises(Exception, match="Rate limit exceeded"):
            client.get_series_data("SERIE1")

def test_sie_client_generic_error():
    client = SIEClient(token="test")
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("error")
        with pytest.raises(Exception, match="error"):
            client.get_series_data("SERIE1")
