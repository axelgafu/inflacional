from dataclasses import dataclass
from datetime import date

@dataclass
class FinanceRecord:
    date: date
    serie_id: str
    value: float
    unit: str = ""
