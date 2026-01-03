from datetime import date
from banxico_report.generators.table import TableGenerator
from banxico_report.models.meeting import MeetingStatus

def test_generate_table():
    gen = TableGenerator()
    data = [{
        'date': date(2026, 1, 1),
        'status': MeetingStatus.PAST,
        'core_inflation': 5.0,
        'annual_inflation': 4.5,
        'inflation_target': "3.0%",
        'target_rate': 11.0,
        'fix_variation': 0.01
    }]
    table = gen.generate_table(data)
    assert "| 2026-01-01 |" in table
    assert "| 5.00 |" in table
    assert "| 4.50 |" in table
