# ADR 0001: API Mocking and Environment Separation

- **Status**: Accepted
- **Date**: 2026-01-02
- **Deciders**: Antigravity, USER

## Context and Problem Statement

To ensure repeatable testing and follow-up development, we need a way to simulate Banxico API communication without incurring rate limits or requiring a valid token during test execution. Production code must remain pure and free of test-specific mock data.

## Decision Drivers

- Test repeatability and reliability.
- Separation of concerns (Production vs. Testing).
- Security (prevent token leaks during testing).

## Considered Options

- **Option 1**: Conditional logic within the service layer (if ENV == 'test'...).
- **Option 2**: Formal interface abstraction (Abstract Base Class) with Provider Factory.

## Decision Outcome

Chosen option: **Option 2**, because it provides strict decoupling, allows for easy extension (e.g., adding other SIE versions), and ensures that production code does not contain any mock logic.

### Consequences

- **Good**: Clean separation, excellent testability, adheres to SOLID principles.
- **Bad**: Slight increase in initial boilerplate (interfaces/factories).
- **Neutral**: Requires environment variable `INFLACIONAL_ENV=test` to activate.

## Rationale

By using an Abstract Base Class (ABC), we define a clear contract for SIE interactions. The Factory ensures that at runtime, the application only knows about the interface, while the specific implementation (Real vs. Mock) is injected based on context.
