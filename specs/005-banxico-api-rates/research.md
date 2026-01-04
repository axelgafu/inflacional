# Research: Banxico API Rates Integration

## Rate Retrieval Strategy

- **Decision**: Implement a look-back loop in `RatesFetcher.get_target_rate` that requests data for the `reference_date` and, if missing, continues seeking data for previous days up to a configurable limit (default 7).
- **Rationale**: The Banxico SIE API `SeriesData` endpoint returns data only for the requested date or range. If the specific date requested is a holiday or weekend, it may return an empty series. A look-back ensures we find the "effective" rate at that point in time.
- **Alternatives Considered**: 
  - Requesting a date range (e.g., `reference_date - 7` to `reference_date`): This reduces API calls but requires more complex client-side parsing. For the MVP, a sequential look-back or a small range request is acceptable. Given `SIEProvider`'s `get_series_data` signature, a range request is actually better to minimize latency.
  - **Revised Decision**: Request a 7-day range ending on `reference_date` and select the latest available data point.

## Parameter Configuration

- **Decision**: Use an environment variable `INFLACIONAL_RATES_LOOKBACK` (default 7) for the look-back window.
- **Rationale**: Keeps the code clean and allows overrides without code changes.

## Error Policy

- **Decision**: Throw a custom `RateRetrievalError` if no data is found after the look-back window.
- **Rationale**: As per clarification, this is a critical failure. A custom exception allows the CLI to catch it and exit with targetted messaging.
