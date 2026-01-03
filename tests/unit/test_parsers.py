from datetime import date
from banxico_report.parsers.calendar import CalendarParser
from banxico_report.models.meeting import MeetingStatus

def test_calendar_parser_get_meetings():
    parser = CalendarParser(year=2026)
    meetings = parser.get_meetings()
    # Mock currently returns 9 meetings (8 + 1 past we added)
    assert len(meetings) >= 8
    assert all(isinstance(m.date, date) for m in meetings)
    
    # Check status logic (1 past meeting was added for 2026-01-01)
    past_meetings = [m for m in meetings if m.status == MeetingStatus.PAST]
    assert len(past_meetings) >= 1

def test_inflation_parser():
    from banxico_report.parsers.inflation import InflationParser
    parser = InflationParser()
    record = parser.get_latest_inflation(date(2026, 1, 1))
    assert record.annual_inflation == 4.66
    assert record.core_inflation == 5.05

def test_target_fetcher():
    from banxico_report.parsers.target import TargetFetcher
    fetcher = TargetFetcher()
    target = fetcher.get_inflation_target()
    assert "3.0%" in target
