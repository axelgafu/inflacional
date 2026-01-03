<!--
Sync Impact Report:
- Version change: [INITIAL] → 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] → I. Security & Privacy First
  - [PRINCIPLE_2_NAME] → II. Quality through BDD & Coverage
  - [PRINCIPLE_3_NAME] → III. Strict API Compliance
  - [PRINCIPLE_4_NAME] → IV. CLI-First Interface
  - [PRINCIPLE_5_NAME] → V. Mandatory Documentation
- Added sections: Technology Stack, Development Standards
- Removed sections: N/A
- Templates requiring updates:
  - .specify/templates/plan-template.md (✅ updated)
  - .specify/templates/spec-template.md (✅ updated)
  - .specify/templates/tasks-template.md (✅ updated)
- Follow-up TODOs: N/A
-->

# inflacional Constitution

## Core Principles

### I. Security & Privacy First
100% data security is mandatory. No sensitive information (secrets, tokens, or PII) shall ever be logged, stored in plain text, or transmitted through external analysis systems (including AI models except where explicitly permitted via secure channels). The `.venv` and environment variables must be strictly isolated to prevent secret leakage.

### II. Quality through BDD & Coverage
Every function and feature MUST be implemented using Behavior-Driven Development (BDD) with the `behave` framework. A minimum of 80% statement coverage for unit testing is required for all deliverables. No feature is considered complete without passing formal acceptance tests.

### III. Strict API Compliance
The project MUST strictly adhere to the official [Banxico SIE REST API v1](https://www.banxico.org.mx/SieAPIRest/service/v1/) and its [Swagger documentation](https://www.banxico.org.mx/SieAPIRest/service/swagger-ui.html#/Series). This includes correct header usage (`Bmx-Token`), response schema validation, and respectful rate limiting handling.

### IV. CLI-First Interface
The main executable MUST provide a robust command-line interface implemented with the `click` library. The CLI should follow standard POSIX conventions for flags, arguments, and exit codes to ensure high usability and interoperability.

### V. Mandatory Documentation
Technical excellence requires clarity. Technical design documentation MUST reside in `doc/design` (covering architecture and data flows), and User documentation MUST reside in `doc/user` (covering setup and execution).

## Technology Stack

The project relies on a modern Python ecosystem:
- **Core**: Python 3.10+
- **CLI**: `click`
- **Testing/BDD**: `behave`, `pytest`, `coverage`
- **API**: `requests`
- **Environment**: `python-dotenv`

## Development Standards

- **Workflow**: Red-Green-Refactor with BDD.
- **Modularity**: Prioritize Usability, Maintainability, and Flexibility in internal components.
- **Error Handling**: Graceful fallbacks for external dependencies (e.g., PDF parsing failures or API downtime).

## Governance

This constitution supersedes all other documentation. Amendments require a version bump and an update to the Sync Impact Report.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
