# Feature Documentation Quickstart

## 1. ADR Creation
When making a significant architectural choice:
1. Copy the NyGard template.
2. Store in `doc/design/adr/` with the next available ID.
3. Link the ADR from `doc/design/architecture.md` if it changes the system overview.

## 2. Technical Design Update
1. Update `doc/design/architecture.md` to reflect new components, entities, or flows.
2. Use Mermaid.js for all technical diagrams (Architecture, Sequence, Class). Ensure labels are quoted and avoid HTML tags.

## 3. User Documentation Update
1. If adding commands or changing config, update `doc/user/manual.md`.
2. Ensure the root `README.md` features are listable and accurate.

## 4. Definition of Done
A feature is done when:
- All new/changed logic is covered by BDD/Unit tests.
- Tech docs are updated in `doc/design/`.
- User docs are updated in `doc/user/` and `README.md`.
