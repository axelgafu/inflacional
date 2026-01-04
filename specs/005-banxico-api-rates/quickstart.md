# Quickstart: Verified Rate Fetching

## 1. Local Testing (Mocks)

Ensure you have a mock file for the target rate:
`tests/mocks/sie/TI52.json`

Run the report in test mode:
```bash
set INFLACIONAL_ENV=test
banxico-report generate
```

## 2. Production Verification

Ensure your `SIE_TOKEN` is set.
```bash
banxico-report generate
```

## 3. Configuration

To change the look-back window (if needed for very old reports):
```bash
set INFLACIONAL_RATES_LOOKBACK=15
banxico-report generate
```

Check the log output (`info`) to verify the date range being requested.
