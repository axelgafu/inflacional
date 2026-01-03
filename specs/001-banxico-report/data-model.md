# Data Model: Banxico Inflation Report Generator

## Entities

### Meeting
| Field | Type | Description |
|-------|------|-------------|
| date | Date | Date of the monetary policy meeting |
| status | Enum | `PAST`, `FUTURE` |
| statement_url | string | Link to the official policy statement (if available) |

### InflationRecord
| Field | Type | Description |
|-------|------|-------------|
| period | string | Month/Half-month of the record |
| annual_inflation | float | % Annual INPC change |
| core_inflation | float | % Annual Core INPC change |
| source_url | string | Link to the INEGI bulletin |

### FinanceRecord
| Field | Type | Description |
|-------|------|-------------|
| date | Date | Reference date |
| serie_id | string | SIE Series ID (e.g., `TI52`, `SF43718`) |
| value | float | The actual value for that date |
| unit | string | `%`, `MXN`, etc. |

### Report
| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique report ID (e.g., timestamp-based) |
| timestamp | DateTime | When the report was generated |
| year | integer | Year being reported |
| meetings | List[MeetingRow] | Aggregated data for the summary table |
| analysis | List[string] | Generated analytical paragraphs |
| references | List[Reference] | APA formatted citations |

## Relationships
- A **Report** contains multiple **MeetingRow** objects.
- Each **MeetingRow** aggregates data from **Meeting**, **InflationRecord**, and multiple **FinanceRecord**s (Target Rate, FIX).
