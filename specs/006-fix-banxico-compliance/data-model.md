# Data Model: Banxico API Compliance

## Entities

### SIEClient (Refined)

The `SIEClient` class is the primary entity responsible for API communication. It does not persist data but manages the state of the connection.

- **Attributes**:
  - `token` (str): The Banxico API token.
  - `tracker` (Optional[MetadataTracker]): For telemetry.
  - `headers` (dict): **UPDATED** to include `{"Bmx-Token": token}` permanently.

- **Methods**:
  - `get_series_data(serie_id, start_date, end_date)`:
    - **Input Validation**: `start_date` and `end_date` must be formatted as `YYYY-MM-DD`.
    - **Request Construction**: Uses `Bmx-Token` header.
    - **URL Structure**: `.../service/v1/series/{serie_id}/datos/{start_date}/{end_date}`.
    - **Response**: Returns JSON with `DD/MM/YYYY` date format.

### API Response Schema (Verified)

```json
{
  "bmx": {
    "series": [
      {
        "idSerie": "SF331451",
        "datos": [
          {
            "fecha": "26/12/2025",  // Format: DD/MM/YYYY
            "dato": "7.09"
          }
        ]
      }
    ]
  }
}
```

## Constants

- `BASE_URL`: `https://www.banxico.org.mx/SieAPIRest/service/v1` (Confirmed correct).
- `SERIE_TARGET_RATE`: `SF331451` (TIIE de Fondeo).
