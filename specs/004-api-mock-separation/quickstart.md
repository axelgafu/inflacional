# Quickstart: Testing with Mocks

## 1. Environment Setup

To enable mocking, set the `INFLACIONAL_ENV` variable to `test`:

```bash
# Windows
set INFLACIONAL_ENV=test

# Unix
export INFLACIONAL_ENV=test
```

## 2. Mock Data Location

Place your simulated JSON responses in:
`tests/mocks/sie/{SERIE_ID}.json`

Example structure for `SP1.json`:
```json
{
  "bmx": {
    "series": [
      {
        "idSerie": "SP1",
        "datos": [
          {"fecha": "01/01/2024", "dato": "130.5"}
        ]
      }
    ]
  }
}
```

## 3. Implementation Check

You can verify the mocking is active by checking the logs. `MockSIEProvider` will log:
`[DEBUG] Using mock data from tests/mocks/sie/{SERIE_ID}.json`

## 4. Production Verification

To ensure production remains pure:
1. Run `pip install .`
2. Check `site-packages/banxico_report/`.
3. Verify that NO `tests/` or `mocks/` directories are present.
