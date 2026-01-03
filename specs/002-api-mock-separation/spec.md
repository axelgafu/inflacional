# Feature Specification: API Mocking and Environment Separation

**Feature Branch**: `002-api-mock-separation`  
**Created**: 2026-01-02  
**Status**: Draft  
**Input**: User description: "Prepara la aplicación para que se pueda simular la comunicación con el API de Banxico y así hacer las pruebas repetibles. No obstante, La aplicación de producción tiene/debe utiliza el api de banxico para obtener datos reales. Es imperante que ambos modos, i.e. testing y producción, estén claramente separados. El modo testing debe configurarse por la infraestructura de pruebas y el de producción debe ser el default en cualquier otra circunstancia. Es mandatorio que no haya código de pruebas en producción, eso es algo que se debe garantizar."

## Clarifications

### Session 2026-01-02

- Q: How should the testing mode be activated? → A: Environment Variable (e.g., `INFLACIONAL_ENV=test`).
- Q: How should the abstraction layer be defined? → A: Formal Interface (Abstract Base Class - `abc.ABC`).
- Q: How should the provider selection be implemented? → A: Factory Pattern (instantiating the appropriate ABC implementation).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Deterministic Testing (Priority: P1)

As a developer, I want to run tests without depending on the real Banxico API, so that my tests are fast, repeatable, and don't fail due to external technical issues or rate limits.

**Why this priority**: It is the core requirement for reliable development and CI/CD. Without this, tests are flaky and depend on external availability.

**Independent Test**: Can be verified by running the test suite in an offline environment (no internet access) and ensuring all tests pass.

**Acceptance Scenarios**:

1. **Given** the testing environment is active, **When** a report is generated during a test run, **Then** the application uses predefined mock data for inflation indices instead of calling the real API.
2. **Given** a specific test case requires a "Data Unavailable" scenario, **When** the test infrastructure configures the mock to return an error, **Then** the application handles the error gracefully as if it came from the real API.

---

### User Story 2 - Safe Production Default (Priority: P1)

As a project owner, I want the application to always use real data by default, so that users don't accidentally receive fake information in the production environment.

**Why this priority**: Essential for data integrity and user trust. Production accuracy is the primary goal of the application.

**Independent Test**: Can be verified by running the installed application in a clean environment without any "test" configuration and observing that it attempts to connect to `datos.banxico.org.mx`.

**Acceptance Scenarios**:

1. **Given** no environment variables or test flags are set, **When** the application starts, **Then** it attempts to connect to the real Banxico SIE API.
2. **Given** the application is running in production mode, **When** an API call is made, **Then** it requires a valid `SIE_TOKEN` and fails if it is missing or invalid.

---

### User Story 3 - Production Purity (Priority: P2)

As a security engineer, I want the production code to be free of test mocks, so that there's no risk of test data leaking into production outputs or increasing the attack surface.

**Why this priority**: Minimizes risks, reduces package size, and ensures that development-only dependencies or data never reach the end user.

**Independent Test**: Can be verified by inspecting the production build or installed package and ensuring no files from `tests/` or mock registries are present in the `src/` hierarchy or site-packages.

**Acceptance Scenarios**:

1. **Given** the application is installed normally (e.g., via `pip install .`), **When** searching for test-specific mock data or mocking utilities in the installed files, **Then** no such files are found.

---

### Edge Cases

- **Mixed Configuration**: If both a Production API token and a Test flag are present, the Test flag (provided by the test runner) MUST take precedence to prevent accidental real API calls during development.
- **Missing Mock Data**: If the system is in Test mode but no mock data is provided for a specific requested series, it MUST raise a clear error indicating the missing test setup rather than falling back to the real API.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST define a formal interface using an Abstract Base Class (ABC) for API calls that allows switching between a "Real Provider" and a "Mock Provider".
- **FR-002**: The system MUST default to the "Real Provider" unless the environment variable `INFLACIONAL_ENV` is set to `test`.
- **FR-003**: The Mock Provider MUST be able to load responses from external files (e.g., JSON or CSV) located within the `tests/` directory.
- **FR-004**: The system MUST NOT import or reference any mocking libraries or test data files within its core modules located in `src/`.
- **FR-005**: A Factory Pattern MUST be used to provide the API client to the application, allowing the system to instantiate the appropriate provider based on the environment configuration while ensuring test-only code remains unimported in production.

### Key Entities *(include if feature involves data)*

- **API Client**: The formal interface (ABC) used by the application to request data from Banxico.
- **Data Provider**: The implementation that fulfills the API Client requests (Real or Mock).
- **Environment Configuration**: The set of parameters that determines which Data Provider to instantiate.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: API calls in the test suite are redirected to mocks, achieving 0% real network calls during `pytest` execution.
- **SC-002**: The application defaults to real API calls with just a standard `pip install` and no extra configuration.
- **SC-003**: Zero "mocking" logic or test-data strings are found within the `src/` directory.
- **SC-004**: Test execution time for API-related modules is reduced by at least 80% compared to real network calls.
