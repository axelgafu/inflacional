# Quickstart: Testing Banxico API Compliance

## Verification Steps

### 1. Verify Header Authentication

Run the unit test to confirm `Bmx-Token` is being sent:

```bash
pytest tests/unit/api/test_sie_client_compliance.py
```

### 2. Verify URL Formatting

Check that dates are effectively formatted as `YYYY-MM-DD`:

```bash
# Debug command (if applicable) or verify via logs
INFLACIONAL_LOG_LEVEL=DEBUG banxico-report generate
```

### 3. End-to-End Validation (Production Mode)

**Prerequisites**: Valid `SIE_TOKEN` in `.env`.

```bash
# PowerShell
$env:INFLACIONAL_ENV="production"; banxico-report generate
```

**Expected Result**:
- No HTTP 400/401 errors.
- Successful report generation with live data.
