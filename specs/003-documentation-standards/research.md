# Research: Documentation Standards and ADRs

## Decision 1: ADR Template
- **Decision**: Adopt the standard NyGard Architectural Decision Record (ADR) template.
- **Rationale**: It is the industry standard for lightweight, version-controlled architectural documentation. It balances brevity with essential context (Title, Status, Context, Decision, Consequences).
- **Alternatives considered**: 
  - **MADR**: More verbose, requires more markdown boilerplate.
  - **Custom format**: Risk of inconsistency and lack of familiarity for new developers.

## Decision 2: Documentation Storage Strategy
- **Decision**: Continuous Global Update.
- **Rationale**: Feature-specific documentation fragments in `specs/` tend to become stale after a branch is merged. Centralizing all "current state" documentation in the `doc/` directory and root `README.md` ensures that developers always find the latest information in a predictable location.
- **Alternatives considered**:
  - **Feature-based folders**: Better for historical record of *work*, but poor for describing *current architecture*.
  - **Wiki-only documentation**: Harder to keep in sync with code changes via PRs.

## Decision 3: ADR Storage Location
- **Decision**: Store ADRs in `doc/design/adr/` as individual numbered markdown files (e.g., `0001-api-mocking.md`).
- **Rationale**: Keeps the architecture overview clean while providing a traceable history of decisions in a subdirectory.
