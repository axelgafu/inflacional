import pytest
from unittest.mock import MagicMock, patch
from banxico_report.generator import ReportGenerator

@patch('banxico_report.generator.get_token', return_value='test')
def test_generator_init(mock_token):
    gen = ReportGenerator()
    assert gen.sie_client is not None
    assert gen.calendar_parser is not None

@patch('banxico_report.generator.get_token', return_value='test')
def test_generator_generate(mock_token):
    gen = ReportGenerator()
    # Mocking behaviors to avoid network calls
    gen.calendar_parser.get_meetings = MagicMock(return_value=[])
    
    report = gen.generate()
    assert "# Reporte de Inflación Banxico" in report
