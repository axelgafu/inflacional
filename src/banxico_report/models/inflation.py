from dataclasses import dataclass

@dataclass
class InflationRecord:
    period: str
    annual_inflation: float
    core_inflation: float
    source_url: str = ""
