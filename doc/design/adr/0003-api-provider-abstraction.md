# ADR 0003: API Provider Abstraction

## Status
Accepted

## Context
The application needs to communicate with the Banxico SIE API to fetch inflation and exchange rate data. To make development and testing more robust, we need a way to simulate these API responses without a real network connection or valid tokens. At the same time, we must ensure that the production environment always uses real data and contains no test-specific code.

## Decision
We decided to implement the **Provider Pattern** using an Abstract Base Class (ABC) named `SIEProvider`.

- **SIEProvider (ABC)** defines the common interface for all data fetchers.
- **RealSIEProvider** implements the interface using the actual `requests`-based client.
- **MockSIEProvider** (located in `tests/`) implements the interface by reading from static JSON mock files.
- **SIEProviderFactory** dynamically selects the implementation based on the `INFLACIONAL_ENV` environment variable (`production` by default).

## Consequences
- **Positive**: 
    - Tests are 100% deterministic and offline-capable.
    - Security is improved as tokens are not needed for development.
    - Production code remains clean (no mocks in `src/`).
- **Negative**:
    - Slight increase in complexity due to the added abstraction layer.
    - Manual maintenance of mock JSON files to keep them in sync with the real API schema.
