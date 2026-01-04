# Feature Specification: API Mocking and Environment Separation

**Feature Branch**: `004-api-mock-separation`  
**Created**: 2026-01-02  
**Status**: Draft  
**Input**: User description: "Prepara la aplicación para que se pueda simular la comunicación con el API de Banxico y así hacer las pruebas repetibles. No obstante, La aplicación de producción tiene/debe utiliza el api de banxico para obtener datos reales. Es imperante que ambos modos, i.e. testing y producción, estén claramente separados. El modo testing debe configurarse por la infraestructura de pruebas y el de producción debe ser el default en cualquier otra circunstancia. Es mandatorio que no haya código de pruebas en producción, eso es algo que se debe garantizar."

## Clarifications

### Session 2026-01-02
- Q: ¿Cuál debería ser el nombre de la variable de entorno para controlar el modo de ejecución? → A: `INFLACIONAL_ENV` (Valores: `production`, `test`). El valor predeterminado es `production`.
- Q: ¿Cómo deben estructurarse y almacenarse los datos utilizados por el `Mock Provider`? → A: Archivos JSON estáticos que repliquen la respuesta exacta del API de Banxico.
- Q: ¿Cómo se debe implementar la exclusión de los mocks en el paquete de producción? → A: Exclusión física por directorio. Los mocks residirán en `tests/mocks/` (fuera de `src/`), y el sistema de empaquetado solo incluirá `src/`.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Deterministic Testing (Priority: P1)

As a developer, I want to run tests using simulated Banxico API data, so that my tests are repeatable, fast, and don't depend on external network availability or API tokens.

**Why this priority**: Essential for reliable CI/CD and developer productivity. Without this, development is blocked by API rate limits and network stability.

**Independent Test**: Can be verified by running the test suite with a specific configuration that overrides the real API client with a mock provider, ensuring no network calls are made.

**Acceptance Scenarios**:

1. **Given** the application is in testing mode, **When** a report is generated, **Then** the application uses mock data instead of calling the Banxico SIE API.
2. **Given** no API token is provided in testing mode, **When** a report is generated, **Then** the application succeeds using simulated data.

---

### User Story 2 - Default Production Integrity (Priority: P1)

As a maintainer, I want the application to use real Banxico data by default in production, so that end-users always receive accurate and up-to-date inflation reports.

**Why this priority**: Core value of the application. Production must be reliable and use live data by default.

**Independent Test**: Can be verified by running the application in a fresh environment (without testing overrides) and observing that it attempts to connect to the actual Banxico API.

**Acceptance Scenarios**:

1. **Given** no environment overrides are set, **When** the application starts, **Then** it defaults to production mode using the real Banxico SIE API.
2. **Given** the application is in production mode, **When** an API call is made, **Then** it must use the configured `SIE_TOKEN` and real endpoints.

---

### User Story 3 - Production Purity (Priority: P2)

As a security-conscious developer, I want to ensure that no test code or mock data is included in the production environment, so that the production footprint is minimized and secure.

**Why this priority**: Security and performance best practice. Prevents accidental leakage of test artifacts into production.

**Independent Test**: Can be verified by auditing the production build/package and ensuring that zero mock-related classes or data files are present in the core application path.

**Acceptance Scenarios**:

1. **Given** a production deployment, **When** the core application package is inspected, **Then** only production-ready code is present.
2. **Given** a production environment, **When** the application is executed, **Then** there is no mechanism to trigger mock behaviors using internal code paths (unless explicitly permitted via external configuration).

---

## Edge Cases

- **Missing Token in Production**: If the application defaults to production but no `SIE_TOKEN` is found, it must error gracefully with instructions rather than falling back to mock data.
- **Incompatible Schema**: If mock data does not match the real API schema, tests should fail, ensuring mocks stay in sync with the real API.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a mechanism to switch between "Production" and "Testing" modes.
- **FR-002**: "Production" mode MUST be the system default.
- **FR-003**: In "Testing" mode, all Banxico SIE API interactions MUST be simulated using static JSON files that replicate the official API response schema.
- **FR-004**: The choice between Production and Testing MUST be controlled by the `INFLACIONAL_ENV` environment variable, defaulting to `production` if unset.
- **FR-005**: Mock implementations and simulation data MUST reside in the `tests/` directory tree, outside of the `src/` production source directory.
- **FR-006**: The production deployment process MUST ensure that only the contents of the `src/` directory (and necessary project metadata) are included, strictly excluding the `tests/` directory.

### Key Entities *(include if feature involves data)*

- **API Provider**: An abstraction representing the ability to fetch data from Banxico.
- **Real Provider**: Implementation that communicates with the actual SIE API.
- **Mock Provider**: Implementation that returns pre-defined simulated data.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of integration tests can run successfully with zero network access.
- **SC-002**: Production code coverage report shows 0% of its statements are related to test-specific mock data generation.
- **SC-003**: A fresh installation without any environment configuration always attempts to connect to the real Banxico API.
- **SC-004**: Test execution time is reduced by at least 50% compared to using a real network-dependent API.
