from datetime import date
from banxico_report.models.meeting import Meeting, MeetingStatus
from banxico_report.models.inflation import InflationRecord

def test_meeting_model():
    m = Meeting(date=date(2026, 1, 1), status=MeetingStatus.PAST)
    assert m.date == date(2026, 1, 1)
    assert m.status == MeetingStatus.PAST

def test_inflation_model():
    inf = InflationRecord("Dic 2025", 4.5, 5.0)
    assert inf.annual_inflation == 4.5
    assert inf.core_inflation == 5.0
