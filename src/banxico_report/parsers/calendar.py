from datetime import date
from ..models.meeting import Meeting, MeetingStatus
from ..utils.logger import setup_logger

logger = setup_logger(__name__)

class CalendarParser:
    def __init__(self, year=2026):
        self.year = year
        
    def get_meetings(self):
        """
        Returns a list of Meeting objects for the given year.
        In a real implementation, this would parse the PDF/HTML from Banxico.
        """
        logger.info(f"Fetching monetary policy meetings for {self.year}")
        
        # Mocking 2026 schedule based on typical Banxico patterns
        meeting_dates = [
            date(2026, 1, 1),
            date(2026, 2, 12),
            date(2026, 3, 26),
            date(2026, 5, 14),
            date(2026, 6, 25),
            date(2026, 8, 13),
            date(2026, 9, 24),
            date(2026, 11, 12),
            date(2026, 12, 17)
        ]
        
        today = date.today()
        meetings = []
        for d in meeting_dates:
            status = MeetingStatus.PAST if d <= today else MeetingStatus.FUTURE
            meetings.append(Meeting(date=d, status=status))
            
        return meetings
