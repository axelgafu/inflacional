# ADR 0002: Documentation Standards and Processes

- **Status**: Accepted
- **Date**: 2026-01-02
- **Deciders**: Antigravity, USER

## Context and Problem Statement

Project documentation often becomes stale or fragmented across multiple folders. We need a standardized way to capture technical decisions and ensure that both user and technical documentation are updated consistently with every feature.

## Decision Drivers

- Maintainability and long-term project health.
- Clear communication for future developers.
- Professional project presentation.

## Considered Options

- **Option 1**: Per-feature documentation fragments in `specs/`.
- **Option 2**: Continuous Global Update in a centralized `doc/` directory with root `README.md`.

## Decision Outcome

Chosen option: **Option 2**, because it provides a single source of truth for the "current state" of the project, making it easier for maintainers to find up-to-date information.

### Consequences

- **Good**: Consistent documentation, professional README, easy discovery of technical choices via ADRs.
- **Bad**: Requires discipline to update global files on every feature branch.
- **Neutral**: Uses NyGard template for ADRs and Mermaid.js for diagrams.

## Rationale

Centralizing documentation in `doc/` and the root `README.md` mirrors the project's source code structure, ensuring that documentation is treated as a first-class citizen and undergoes the same review process as code.
