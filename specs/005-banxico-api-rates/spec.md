# Feature Specification: Banxico API Rates Integration

**Feature Branch**: `005-banxico-api-rates`  
**Created**: 2026-01-02  
**Status**: Draft  
**Input**: User description: "use banxico api - get_target_rate of src/banxico_report/api/rates.py script should use the banxico API not return hardcoded data."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Real-time Interest Rate (Priority: P1)

As an analyst, for the production path, I want the report to show the actual target interest rate from Banxico for the meeting date, so that the report contains accurate and official information.

**Why this priority**: Correct interest rate data is a core requirement for inflation reports. Using hardcoded data makes the report unreliable and unprofessional.

**Independent Test**: Can be verified by running the report in `test` mode with unique mock data for series `TI52` and confirming the output matches the mock instead of the hardcoded `10.25`.

**Acceptance Scenarios**:

1. **Given** the application is configured with a valid `SIE_TOKEN`, **When** a report is generated for a specific date, **Then** the application fetches the target rate from the Banxico SIE API using series `TI52`.
2. **Given** the application is in testing mode, **When** a report is generated, **Then** the `MockSIEProvider` is called to retrieve simulated interest rate data.

---

### User Story 2 - Robust Data Retrieval (Priority: P2)

As a developer, I want the system to handle missing or errored API data gracefully, so that the user receives an informative message instead of a crash or incorrect data.

**Why this priority**: Enhances system reliability and user trust.

**Independent Test**: Can be verified by simulating a 404 or empty response from the provider and checking that the application logs the error correctly.

**Acceptance Scenarios**:

1. **Given** the Banxico API is unavailable, **When** a rate is requested, **Then** the system raises a descriptive error informing about the communication failure.
2. **Given** the requested date has no data in the API, **When** a rate is requested, **Then** the system searches for the nearest preceding available data point or reports the absence clearly.

---

## Edge Cases

- **Non-Business Days**: If a meeting date falls on a weekend or holiday, the system must fetch the rate effective on that day (which usually corresponds to the last available business day's rate).
- **Incomplete API Response**: Handling cases where the JSON structure returned by Banxico is valid but missing the expected data fields.

## Clarifications

### Session 2026-01-02
- Q: ¿Cuál es el número máximo de días que el sistema debe buscar hacia atrás para encontrar una tasa de interés válida? → A: Hazlo configurable con un default de 7 días.
- Q: ¿Cómo debe reaccionar el sistema ante el fracaso total en la obtención de la tasa TI52? → A: Fallo Crítico: Detener la generación del reporte y lanzar error.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: `RatesFetcher.get_target_rate` MUST utilize the `SIEProvider` instance passed during initialization.
- **FR-002**: The fetcher MUST request series `TI52` from the provider.
- **FR-003**: The fetcher MUST provide the `reference_date` to the provider and implement a configurable look-back window (default 7 days) to find the nearest preceding available data point if the exact date is missing.
- **FR-004**: The system MUST parse the API response to extract the numeric rate value, handling the nested JSON structure of the SIE API.
- **FR-005**: Hardcoded values (specifically `10.25`) MUST be removed from the production path of `RatesFetcher`.

### Key Entities *(include if feature involves data)*

- **RatesFetcher**: The component responsible for orchestrating the retrieval of interest rates.
- **SIEProvider**: The abstraction layer (Real/Mock) used to communicate with the data source.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of interest rate values in generated reports originate from the `SIEProvider` response.
- **SC-002**: Report generation fails explicitly if data for series `TI52` cannot be retrieved, ensuring no silent hardcoded fallbacks.
- **SC-003**: Automated integration tests confirm that changing mock data for `TI52` results in corresponding changes in the `RatesFetcher` output.
