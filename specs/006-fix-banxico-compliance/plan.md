# Implementation Plan: Banxico API Compliance Fix

**Branch**: `006-fix-banxico-compliance` | **Date**: 2026-01-03 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/006-fix-banxico-compliance/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

## Summary

✅ **COMPLETED**: Enforced `Bmx-Token` header for authentication and strict `YYYY-MM-DD` date format in URLs to resolve API 400/401 errors. Updated technical documentation to reference official sources.

## Technical Context

**Language/Version**: Python 3.10+
**Primary Dependencies**: `requests`, `python-dotenv`
**Storage**: N/A
**Testing**: `behave`, `pytest`, `requests-mock`
**Target Platform**: CLI
**Project Type**: single
**Performance Goals**: N/A
**Constraints**: Zero changes to existing robust retry logic; only auth/URL format changes.
**Scale/Scope**: Affects all external API calls.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Rationale |
|-----------|--------|-----------|
| I. Security & Privacy | ✅ PASS | Uses secure headers for tokens instead of query params (more secure). |
| II. Quality & BDD | ✅ PASS | BDD scenarios defined for compliance verification. |
| III. API Compliance | ✅ PASS | This entire feature IS the implementation of Principle III. |
| IV. CLI-First | ✅ PASS | N/A (Internal plumbing). |
| V. Documentation | ✅ PASS | Documentation updates are part of the scope. |

## Project Structure

### Documentation (this feature)

```text
specs/006-fix-banxico-compliance/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── adr.md               # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output
```

### Source Code (repository root)

```text
src/
└── banxico_report/
    └── api/
        └── sie_client.py  # MODIFIED: Header auth & URL formatting logic
```

**Structure Decision**: Minimal invasive change to `sie_client.py` only.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | | |
