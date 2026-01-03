import pytest
from unittest.mock import MagicMock, patch
from banxico_report.parsers.pdf_util import extract_tables_from_pdf, extract_text_from_pdf

@patch('pdfplumber.open')
def test_extract_tables(mock_open):
    mock_pdf = MagicMock()
    mock_page = MagicMock()
    mock_page.extract_tables.return_value = [["table"]]
    mock_pdf.pages = [mock_page]
    mock_open.return_value.__enter__.return_value = mock_pdf
    
    result = extract_tables_from_pdf("dummy.pdf")
    assert result == [["table"]]

@patch('pdfplumber.open')
def test_extract_text(mock_open):
    mock_pdf = MagicMock()
    mock_page = MagicMock()
    mock_page.extract_text.return_value = "hello"
    mock_pdf.pages = [mock_page]
    mock_open.return_value.__enter__.return_value = mock_pdf
    
    result = extract_text_from_pdf("dummy.pdf")
    assert "hello" in result

@patch('pdfplumber.open')
def test_extract_text_error(mock_open):
    mock_open.side_effect = Exception("error")
    with pytest.raises(Exception):
        extract_text_from_pdf("dummy.pdf")
