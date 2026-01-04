# ADR 0005: Strict Banxico API Compliance

## Status
Accepted

## Context
The application was encountering HTTP 400/401 errors when communicating with the Banxico SIE API. Analysis revealed inconsistencies between our request format (query parameters vs headers) and the official V1 API documentation.

## Decision
1. **Authentication**: Switch strictly to the `Bmx-Token` HTTP header. Eliminate usage of the `token` query parameter for the REST API.
2. **Date Formatting**: Enforce `YYYY-MM-DD` (ISO 8601) format for all path parameters (`fechaIni`, `fechaFin`).
3. **Base URL**: Hardcode the reliable V1 base URL (`https://www.banxico.org.mx/SieAPIRest/service/v1`).

## Rationale
- **Security**: Headers are not logged in server access logs (unlike URLs), making `Bmx-Token` the secure choice.
- **Compliance**: Banxico's Swagger documentation explicitly defines `Bmx-Token` as the authentication mechanism.
- **Reliability**: Using the exact specified format reduces the risk of rejection by the API gateway.

## Consequences
- `SIEClient` must be updated to modify its header construction logic.
- Existing tests mocking the API might need updates if they asserted query parameters.
