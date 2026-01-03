from dataclasses import dataclass
from datetime import date
from enum import Enum

class MeetingStatus(Enum):
    PAST = "PAST"
    FUTURE = "FUTURE"

@dataclass
class Meeting:
    date: date
    status: MeetingStatus
    statement_url: str = ""
