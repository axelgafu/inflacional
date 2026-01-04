# ADR 0004: Interest Rate Look-back Strategy

## Status
Accepted

## Context
The Banxico SIE API returns interest rate data for specific dates. However, inflation reports may be generated on holidays or weekends when no target rate is published for that specific day. To ensure the report has official data, we need a way to find the "effective" rate at that point in time.

## Decision
Implement a configurable look-back window (default 7 days). When requesting the target interest rate (series `TI52`), the system will request a range from `reference_date - lookback_window` to `reference_date`. The system will then select the latest available observation from this range.

If no data is found after the look-back window, the system will raise a critical failure (`RateRetrievalError`) to maintain data integrity.

## Rationale
- **Accuracy**: Selecting the latest available data point ensures we use the most recent official mandate.
- **Robustness**: Handles weekends and bank holidays automatically.
- **Transparency**: A configurable look-back allows users to adjust for unusual data gaps without changing code.
- **Fail-fast**: Raising an error prevents the report from silently using incorrect or missing data.

## Consequences
- The system makes a range request instead of a single-date request, which is handled efficiently by the Banxico API.
- Users can override the window via the `INFLACIONAL_RATES_LOOKBACK` environment variable.
