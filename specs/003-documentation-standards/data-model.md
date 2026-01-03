# Documentation Data Model

## Entities

### Architecture Decision Record (ADR)
- **ID**: `Sequential number (0001, 0002, ...)`
- **Title**: `Descriptive decision name`
- **File Path**: `doc/design/adr/{ID}-{Title-Slug}.md`
- **Sections**:
  - `Status`: Proposed | Accepted | Deprecated | Superseded
  - `Context`: Background and problem description
  - `Decision`: Implementation choice
  - `Consequences`: Impact (Pros/Cons)

### Architecture Overview
- **File Path**: `doc/design/architecture.md`
- **Content**: High-level system design, module interactions, and core components.

### User Manual
- **File Path**: `doc/user/manual.md`
- **Content**: Detailed setup, configuration, and execution instructions for end-users.

### Onboarding Checklist
- **File Path**: `doc/user/onboarding.md`
- **Content**: A step-by-step verification list for new developers to validate their understanding of the architecture.

### Project Presence (README)
- **File Path**: `README.md`
- **Content**: Professional "front-door" summary for developers and domain experts.
