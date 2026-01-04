# Feature Specification: Banxico API Compliance Fix

**Feature Branch**: `006-fix-banxico-compliance`
**Created**: 2026-01-03
**Status**: Draft
**Input**: User description: "Las solicitudes REST al API de Banxico están fallando porque no siguen la documentación correcta. Revisa la siguiente documentación y realiza las configuraciones requeridas, también actualiza la documentación técnica para que apunte a la documentación del API de Banxico una vez que se confirme su fucionalidad"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Compliant API Requests (Priority: P1)

As a developer, I want the system to send HTTP requests that strictly adhere to the Banxico SIE API documentation, so that authentication and data retrieval succeed reliably without 400/401 errors.

**Why this priority**: The current implementation is failing due to non-compliance, blocking the core functionality of fetching interest rates.

**Independent Test**: Can be verified by running the `RatesFetcher` integration test against the real API (with a valid token) and confirming a 200 OK response with valid JSON data, instead of an error.

**Acceptance Scenarios**:

1. **Given** a valid `SIE_TOKEN` in the environment, **When** the system makes a request to the Banxico API, **Then** the request includes the `Bmx-Token` header exactly as specified in the documentation.
2. **Given** a data request, **When** the URL is constructed, **Then** it follows the structure `/SieAPIRest/service/v1/series/{idSerie}/datos/{fechaIni}/{fechaFin}` (or the appropriate endpoint for range/point data).

---

### User Story 2 - Documentation Alignment (Priority: P2)

As a maintainer, I want the internal technical documentation to explicitly reference the official Banxico API v1 documentation, so that future contributors have the correct source of truth.

**Why this priority**: Prevents future regressions and confusion about where to find the API definition.

**Independent Test**: Verify that `doc/design/architecture.md` (or relevant doc) contains valid links to `https://www.banxico.org.mx/SieAPIRest/service/v1/`.

**Acceptance Scenarios**:

1. **Given** the project documentation, **When** a developer checks the Data Source section, **Then** they find a direct link to the official Banxico SIE API v1 documentation.

---

## Clarifications

### Session 2026-01-03
- Q: Header de Autenticación exacto → A: `Bmx-Token`
- Q: Formato de Fecha en URL → A: `YYYY-MM-DD`

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The `SIEClient` MUST send the API token using the `Bmx-Token` HTTP header.
- **FR-002**: The `SIEClient` MUST NOT use query parameters for authentication (if currently doing so) unless supported/required as fallback; header is preferred/mandatory.
- **FR-003**: API requests MUST use the correct base URL `https://www.banxico.org.mx/SieAPIRest/service/v1/` and `YYYY-MM-DD` date format. Target Series ID MUST be `SF331451` (TIIE de Fondeo).
- **FR-004**: Technical documentation MUST be updated to reference the official Banxico API documentation URL.
- **FR-005**: Application MUST parse API error responses to provide actionable user feedback (e.g., distinguishing auth errors from data errors).

### Key Entities

- **SIEClient**: The low-level HTTP client responsible for formatting requests.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of valid production API requests return HTTP 200 OK.
- **SC-002**: Elimination of HTTP 401 (Unauthorized) errors caused by incorrect header format.
- **SC-003**: The project documentation contains the correct reference link to the Banxico API.
