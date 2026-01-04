# Data Model: Rates Integration

## Entities

### RatesFetcher (Updated)
- **Attributes**:
  - `provider`: `SIEProvider`
  - `lookback_window`: `int` (default 7)
- **Methods**:
  - `get_target_rate(reference_date: date) -> float`
    - Logic:
      1. Calculate `start_date` as `reference_date - lookback_window`.
      2. Call `provider.get_series_data(SERIE_TARGET_RATE, start_date, reference_date)`.
      3. Parse the `datos` array.
      4. Find the observation with the date closest to (and not after) `reference_date`.
      5. Return the numeric value.
      6. Raise `RateRetrievalError` if no data points exist in the range.

## Constants
- `SERIE_TARGET_RATE`: "TI52"
