# Research: Banxico API Compliance

## Authentication Strategy

- **Decision**: Use `Bmx-Token` HTTP Header exclusively.
- **Rationale**: Official Banxico documentation and standard REST security practices favor headers over query parameters to avoid logging secrets in URLs. 
- **Alternatives Considered**: 
  - Query Parameter `token`: Easier to implement but less secure and explicitly discouraged by `FR-002`.

## Date Formatting

- **Decision**: Enforce `YYYY-MM-DD` (ISO 8601) for all date path parameters.
- **Rationale**: Banxico API v1 expects this specific format for `fechaIni` and `fechaFin`.
- **Alternatives Considered**: 
  - `dd-mm-yyyy`: Common in Mexico but rejected by this specific REST endpoint.

## Verification

- **Strategy**: Use `requests-mock` to verify headers in unit tests without hitting the real API, and `RealSIEProvider` integration tests for end-to-end confirmation.
