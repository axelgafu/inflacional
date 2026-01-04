# Research: API Mocking and Environment Separation

## Abstraction Pattern

- **Decision**: Implement an Abstract Base Class (ABC) named `SIEProvider`.
- **Rationale**: Defines a clear contract that both the real API client and the mock client must follow. This ensures that the caller (`ReportGenerator`) doesn't need to know which implementation it's using.
- **Alternatives Considered**: 
  - Monkeypatching `requests` in tests: Rejected because it leaks test logic into the production runtime if not handled carefully, and it's less typesafe.
  - Dependency Injection (DI) frameworks: Rejected to keep the codebase lightweight and dependency-minimal.

## Environment Detection

- **Decision**: Use `os.getenv("INFLACIONAL_ENV", "production")`.
- **Rationale**: Standard practice in Python ecosystems. Defaulting to `production` ensures safety.
- **Implementation**: A `SIEProviderFactory` will encapsulate the switching logic.

## Production Purity (Packaging)

- **Decision**: Rely on `setuptools` package discovery limited to the `src/` directory.
- **Rationale**: The current `pyproject.toml` configuration (`[tool.setuptools.packages.find] where = ["src"]`) already excludes the `tests/` directory from being included in the distributive package (wheel/sdist), as `tests/` is a sibling to `src/`.
- **Verification**: Will run `python -m build` (if requested) to verify the wheel content excludes `tests/mocks/`.

## Mock Data Management

- **Decision**: Store raw JSON dumps in `tests/mocks/sie/`.
- **Rationale**: Easy to update by simply saving a real API response. `MockSIEProvider` will use `pathlib` for robust path resolution regardless of the current working directory during test execution.
