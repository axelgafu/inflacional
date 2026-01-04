# Data Model: API Providers

## Entities

### SIEProvider (Interface)
- **Purpose**: Defines the contract for fetching data from Banxico.
- **Methods**:
  - `get_series_data(serie_id: str, start_date: str = None, end_date: str = None) -> dict`

### RealSIEProvider (Implementation)
- **Role**: Concrete implementation communicating with the live REST API.
- **Dependencies**: `requests`, `Bmx-Token`.
- **Behavior**: Throws `HTTPError` on failure, handles rate limits.

### MockSIEProvider (Implementation)
- **Role**: Simulation client for testing.
- **Source**: Reads from `tests/mocks/sie/{serie_id}.json`.
- **Behavior**: Returns parsed JSON content. Throws `FileNotFoundError` if mock data is missing for a requested ID.

### SIEProviderFactory
- **Role**: Singleton/Static factory for instantiating the appropriate provider.
- **Selection Logic**:
  - if `INFLACIONAL_ENV == "test"` → `MockSIEProvider`
  - else → `RealSIEProvider`
