# Tasks: API Mocking and Environment Separation

**Input**: Design documents from `/specs/004-api-mock-separation/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and mock storage preparation

- [x] T001 Create mock storage directory `tests/mocks/sie/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core abstraction and factory infrastructure

- [x] T002 Implement `SIEProvider` ABC in `src/banxico_report/api/provider.py`
- [x] T003 Implement `SIEProviderFactory` with environment switching logic in `src/banxico_report/api/factory.py`

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Deterministic Testing (Priority: P1) 🎯 MVP

**Goal**: Enable repeatable tests using static JSON mock data.

**Independent Test**: Run a test that requests SIE data with `INFLACIONAL_ENV=test` and verify it loads the JSON from `tests/mocks/sie/` without network access.

### Integration & BDD Tests for User Story 1

- [x] T004 [P] [US1] Create BDD feature file `features/environment_switching.feature` defining mode selection logic
- [x] T005 [P] [US1] Create integration test `tests/integration/test_mock_provider.py` verifying mock data loading

### Implementation for User Story 1

- [x] T006 [P] [US1] Create sample mock JSON in `tests/mocks/sie/SP1.json`
- [x] T007 [P] [US1] Implement `MockSIEProvider` in `tests/mocks/provider.py` (Resides in `tests/` per FR-005)

**Checkpoint**: User Story 1 (Mocking) is fully functional and testable.

---

## Phase 4: User Story 2 - Default Production Integrity (Priority: P1)

**Goal**: Ensure production usage by default and migrated existing logic to the provider pattern.

**Independent Test**: Running the app without overrides should attempt to contact the real Banxico API.

### Implementation for User Story 2

- [x] T008 [US2] Implement `RealSIEProvider` in `src/banxico_report/api/real.py` (Migrate logic from `sie_client.py`)
- [x] T009 [US2] Update `ExchangeRateFetcher` in `src/banxico_report/api/exchange.py` to use `SIEProvider` type-hint
- [x] T010 [US2] Update `RatesFetcher` in `src/banxico_report/api/rates.py` to use `SIEProvider` type-hint
- [x] T011 [US2] Integrate `SIEProviderFactory` into `cli.py` and `generator.py` to inject the correct provider

**Checkpoint**: User Story 2 (Production transition) is complete.

---

## Phase 5: User Story 3 - Production Purity (Priority: P2)

**Goal**: Guarantee no test artifacts reach the production environment.

**Independent Test**: Verify that `pip install .` does not include the `tests/` directory in the installed package.

### Implementation for User Story 3

- [x] T012 [US3] Verify `pyproject.toml` configuration and setuptools discovery rules to strictly exclude `tests/`

---

## Phase 6: Polish & Cross-Cutting Concerns

- [x] T013 [P] Create ADR 0003: API Provider Abstraction in `doc/design/adr/0003-api-provider-abstraction.md`
- [x] T014 [P] Update `doc/design/architecture.md` with Provider pattern Mermaid diagram
- [x] T015 [P] Update `README.md` with `INFLACIONAL_ENV` and `tests/mocks` documentation
- [x] T016 Run `quickstart.md` validation tasks

---

## Dependencies & Execution Order

### Phase Dependencies
- **Setup & Foundational (Phases 1-2)**: Work starts here. Blocks all user stories.
- **User Stories (Phases 3-4)**: Can proceed in parallel once Phase 2 is complete.
- **Production Purity (Phase 5)**: Final verification step.
- **Polish (Phase 6)**: Final documentation and cleanup.

### Parallel Opportunities
- All [P] tasks within their respective phases.
- US1 (Phase 3) and US2 (Phase 4) can be worked on concurrently if infrastructure is ready.

---

## Implementation Strategy

### MVP First (User Story 1 Focus)
1. Complete Setup + Foundational.
2. Implement US1 (Mocking) to unblock all other development from API dependency.
3. Validate US1 independently.

### Incremental Delivery
- US1: Developer unblocking.
- US2: Production stability.
- US3: Security & packaging compliance.
