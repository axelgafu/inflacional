# Tasks: Banxico API Rates Integration

**Input**: Design documents from `/specs/005-banxico-api-rates/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)

---

## Phase 1: Setup

**Purpose**: Infrastructure preparation

- [ ] T001 [P] Ensure mock data exists for testing in `tests/mocks/sie/TI52.json`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core logic and configuration baseline

- [ ] T002 Implement custom exception `RateRetrievalError` in `src/banxico_report/utils/errors.py`
- [ ] T003 Implement configuration utility for `INFLACIONAL_RATES_LOOKBACK` in `src/banxico_report/utils/config.py`

---

## Phase 3: User Story 1 - Real-time Interest Rate (Priority: P1) 🎯 MVP

**Goal**: Fetch target rate from SIE API using series `TI52`.

**Independent Test**: Running the app in `test` mode should return values from `TI52.json` instead of hardcoded `10.25`.

### BDD Scenarios for User Story 1

- [ ] T004 [P] [US1] Create BDD feature file `tests/features/rates_fetching.feature`
- [ ] T005 [US1] Implement BDD step definitions in `tests/features/steps/rates_fetching_steps.py`

### Integration Tests for User Story 1

- [ ] T006 [P] [US1] Create integration test `tests/integration/test_rates_mock.py` verifying mock data retrieval

### Implementation for User Story 1

- [ ] T007 [US1] Refactor `RatesFetcher.get_target_rate` in `src/banxico_report/api/rates.py` to use `self.provider.get_series_data`

---

## Phase 4: User Story 2 - Robust Data Retrieval (Priority: P2)

**Goal**: Implement look-back logic and graceful error handling.

**Independent Test**: Verify that the system fetches data for preceding days if the meeting date is a holiday.

### Unit Tests for User Story 2

- [ ] T008 [P] [US2] Create unit tests in `tests/unit/api/test_rates_logic.py` for look-back date calculation and range selection

### Implementation for User Story 2

- [ ] T009 [US2] Implement date range request and selection logic in `RatesFetcher.get_target_rate`
- [ ] T010 [US2] Implement critical failure policy (raising `RateRetrievalError`) if no data is found within window

---

## Phase 5: Polish & Cross-Cutting Concerns

- [ ] T011 [P] Create ADR 0004: Interest Rate Look-back Strategy in `doc/design/adr/0004-rates-lookback.md`
- [ ] T012 [P] Update `README.md` with `INFLACIONAL_RATES_LOOKBACK` documentation
- [ ] T013 Run `quickstart.md` validation tasks

---

## Dependencies & Execution Order

### Phase Dependencies
- **Setup & Foundational (Phases 1-2)**: Work starts here. Blocks US implementation.
- **US1 (Phase 3)**: Enables basic API-driven rates.
- **US2 (Phase 4)**: Adds robustness and handles edge cases. Blocks final release.
- **Polish (Phase 5)**: Documentation and final cleanup.

### Parallel Opportunities
- All [P] tasks can run concurrently if their respective phase is active.
- T004 can start as soon as T001 is ready.
- T006 can start as soon as T002/T003 are ready.

---

## Implementation Strategy

### MVP First (User Story 1 Focus)
1. Complete Foundational tasks (Exceptions/Config).
2. Implement US1 to get real data flowing.
3. Verify US1 with integration tests.

### Incremental Delivery
- **US1**: Core functionality (Bye bye hardcoded values).
- **US2**: Stability and edge case handling (Non-business days).
- **Polish**: Compliance and documentation.
