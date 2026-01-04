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
    - **URL Structure**: `.../series/{serie_id}/datos/{start_date}/{end_date}`.

## Constants

- `BASE_URL`: `https://www.banxico.org.mx/SieAPIRest/service/v1` (Confirmed correct).
