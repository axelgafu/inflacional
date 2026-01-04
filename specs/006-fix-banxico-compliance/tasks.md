# Tasks: Banxico API Compliance Fix

**Input**: Design documents from `/specs/006-fix-banxico-compliance/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, quickstart.md, adr.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)

---

## Phase 1: Setup

**Purpose**: Infrastructure preparation

- [x] T001 [P] Ensure environment is verified for new feature branch

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core configuration changes

- [x] T002 Update `src/banxico_report/api/sie_client.py` to add `Bmx-Token` header and refine `get_series_data` signature/calls

---

## Phase 3: User Story 1 - Compliant API Requests (Priority: P1)

**Goal**: Ensure all API requests use correct headers and date formats.

**Independent Test**: Unit test `test_sie_client_compliance.py` passes.

### Tests for User Story 1

- [x] T003 [P] [US1] Create unit test `tests/unit/api/test_sie_client_compliance.py` verifying header presence and URL format (TDD)

### Implementation for User Story 1

- [x] T004 [US1] [P] Refactor `SIEClient` class in `src/banxico_report/api/sie_client.py` to strictly enforce `Bmx-Token` header
- [x] T005 [US1] Refactor `SIEClient.get_series_data` in `src/banxico_report/api/sie_client.py` to enforce `YYYY-MM-DD` date format in URL path

### Integration

- [x] T006 [US1] Verify compliance by running `RatesFetcher` integration tests against real API

---

## Phase 4: User Story 2 - Documentation Alignment (Priority: P2)

**Goal**: Align internal docs with official Banxico documentation.

### Implementation for User Story 2

- [x] T007 [P] [US2] Update `doc/design/architecture.md` (and verify others) to reference official Banxico API v1 documentation and removing obsolete examples if any

---

## Phase 5: Polish & Cross-Cutting Concerns

- [x] T008 [P] Update `README.md` if any strictly API-related config instructions changed (unlikely but check)
- [x] T009 Run `quickstart.md` validation tasks

---

## Dependencies & Execution Order

### Phase Dependencies
- **Setup (Phase 1)**: Trivial.
- **Foundational (Phase 2)**: T002 is essentially the start of US1 implementation.
- **US1 (Phase 3)**: Critical path.
- **US2 (Phase 4)**: Can happen anytime after planning.
- **Polish (Phase 5)**: Final cleanup.

### Parallel Opportunities
- T003 (Test creation) and T007 (Docs update) and T008 (Review) can run in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Focus)
1. Write failing test for compliance (T003).
2. Fix `SIEClient` (T004/T005).
3. Verify.

### Incremental Delivery
- **US1**: Functional Fix.
- **US2**: Documentation Fix.
