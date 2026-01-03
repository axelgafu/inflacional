# Tasks: Banxico Inflation Report Generator

**Input**: Design documents from `specs/001-banxico-report/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: BDD (behave) and Unit Tests (pytest) are MANDATORY as per Constitution Principle II.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing. US1 is the MVP.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and repository structure

- [X] T001 Create project structure per implementation plan (src/, tests/, doc/)
- [X] T002 Initialize Python project with `requirements.txt` (click, behave, requests, etc.)
- [X] T003 [P] Configure `.gitignore` and `.env.template` (SIE_TOKEN=)
- [X] T004 [P] Configure linting (ruff) and coverage tools

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [X] T005 Implement environment configuration management in `src/banxico_report/utils/config.py`
- [X] T006 [P] Implement base SIE API client using `requests` in `src/banxico_report/api/sie_client.py`
- [X] T007 [P] Implement PDF parsing utility using `pdfplumber` in `src/banxico_report/parsers/pdf_util.py`
- [X] T008 Setup logging infrastructure in `src/banxico_report/utils/logger.py`
- [X] T009 Create base data models (Meeting, InflationRecord) in `src/banxico_report/models/`

**Checkpoint**: Foundation ready - US1 implementation can now begin.

---

## Phase 3: User Story 1 - Generate Report Table (Priority: P1) 🎯 MVP

**Goal**: Automatically generate a Spanish Markdown table summarizing Banxico meetings (Dates, Inflation, Target Rate, FIX variation).

**Independent Test**: Run `python -m banxico_report generate` and verify a valid Markdown table is printed with 2026 meeting data.

### Tests for User Story 1
- [X] T010 [P] [US1] Create BDD feature file for report table in `tests/features/report_table.feature`
- [X] T011 [P] [US1] Create step definitions for API responses in `tests/features/steps/api_steps.py`
- [X] T012 [P] [US1] Write unit tests for FIX calculation logic in `tests/unit/test_calculations.py`

### Implementation for User Story 1
- [X] T013 [US1] Implement Banxico Calendar parser in `src/banxico_report/parsers/calendar.py`
- [X] T014 [US1] Implement INEGI Inflation parser in `src/banxico_report/parsers/inflation.py`
- [X] T015 [US1] Implement Target Interest Rate fetcher in `src/banxico_report/api/rates.py` (Series TI52)
- [X] T015b [US1] Implement Inflation Target fetcher (3.0% logic) in `src/banxico_report/parsers/target.py`
- [X] T016 [US1] Implement FIX Rate fetcher with $t-1$ logic and 4-decimal precision in `src/banxico_report/api/exchange.py` (Series SF43718)
- [X] T017 [US1] Implement Table Generator in `src/banxico_report/generators/table.py`
- [X] T018 [US1] Create CLI entry point using `click` in `src/banxico_report/cli.py`
- [X] T019 [US1] Implement file persistence with timestamped names in `src/banxico_report/utils/persistence.py`

**Checkpoint**: User Story 1 is functional. The system can generate and save the summary table.

---

## Phase 4: User Story 2 - Analytical Insights and References (Priority: P2)

**Goal**: Include rule-based analytical paragraphs and full APA references in the report.

**Independent Test**: Verify the generated report contains sections "Análisis" and "Referencias" with correct data and formatting.

### Tests for User Story 2
- [X] T020 [P] [US2] Create BDD feature file for insights and references in `tests/features/insights_refs.feature`
- [X] T021 [P] [US2] Write unit tests for APA formatter in `tests/unit/test_apa.py`
- [X] T022 [P] [US2] Write unit tests for rule engine logic in `tests/unit/test_rule_engine.py`

### Implementation for User Story 2
- [X] T023 [US2] Implement deterministic rule engine using `string.Template` in `src/banxico_report/templates/engine.py`
- [X] T024 [US2] Create Spanish templates for financial insights in `src/banxico_report/templates/insights_es.py`
- [X] T025 [US2] Implement APA Reference Formatter in `src/banxico_report/generators/references.py`
- [X] T026 [US2] Update Report Generator to include Analysis and References sections in `src/banxico_report/generator.py`
- [X] T027 [US2] Integrate API call recording for technical metadata in `src/banxico_report/utils/metadata.py`

**Checkpoint**: User Story 2 is functional. The report is complete according to the logical structure.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Documentation, performance, and validation across all concerns.

- [X] T028 [P] Complete Technical Design documentation in `doc/design/architecture.md`
- [X] T030 Perform final coverage audit (Target: 80%+) and fix gaps
- [X] T030b Validate all success criteria (SC-001 to SC-004) against final outputs
- [X] T031 Validate `quickstart.md` steps in a clean environment
- [X] T032 [P] Optimize API calls with basic caching in `src/banxico_report/api/cache.py`
- [X] T033 Code cleanup and compliance check against Project Constitution
- [X] T029 [P] Complete User Documentation and setup guide in `doc/user/manual.md`

---

## Dependencies & Execution Order

### Phase Dependencies
- **Phase 1**: No dependencies.
- **Phase 2**: Depends on Setup (Phase 1).
- **Phase 3 (US1)**: Depends on Foundational (Phase 2).
- **Phase 4 (US2)**: Depends on Phase 3 completion (data must be available for analysis).
- **Phase 5**: Depends on all User Stories.

### Parallel Opportunities
- T003, T004 (Setup phase)
- T006, T007 (Foundational tools)
- T010-T012 (US1 tests)
- T020-T022 (US2 tests)
- Documentation tasks in Phase 5.

---

## Parallel Example: User Story 1
```bash
# Prepare all tests concurrently
Task: "Create BDD feature file and step definitions"
Task: "Write unit tests for calculation logic"

# Implement data fetchers concurrently
Task: "Implement Target Rate fetcher (TI52)"
Task: "Implement FIX Rate fetcher (SF43718)"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)
1. Initialize structure and dependencies.
2. Implement SIE Client and PDF utilities.
3. Build the primary table generator and CLI.
4. **STOP**: Verify Spanish table generation with real/mock data.

### Incremental Delivery
1. Foundation -> Stable core.
2. US1 -> Reliable data extraction and CSV/MD table.
3. US2 -> Professional reporting with insights and academic rigor.
4. Polish -> Documentation and 80%+ coverage assurance.
