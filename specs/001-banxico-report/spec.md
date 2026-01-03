# Feature Specification: Banxico Inflation Report Generator

**Feature Branch**: `001-banxico-report`  
**Created**: 2026-01-02  
**Status**: Draft  
**Input**: User description: "Expert implementation of a Banxico inflation report generator using SIE REST API and official sources (Banxico, INEGI)."

## Clarifications

### Session 2026-01-02
- Q: Which specific Python BDD framework should be used? → A: `behave` (Standard Gherkin-based BDD).
- Q: How to determine day `t-1` for FIX variation on Mondays/Holidays? → A: Use the nearest preceding business day found in SIE series.
- Q: How should the analytical paragraphs be generated (considering AI security)? → A: Rule-based template engine (Deterministic/Private).
- Q: Should the output be persisted? → A: Yes, mirrored to a file with a precise timestamp in the name.
- Q: What additional metadata is needed for reproducibility? → A: The exact API call/command used to fetch data from Banxico.
- Q: What is the expected tone of the report content? → A: Formal (like a financial advisor), Simple (accessible to non-experts), and Neutral.
- Q: What is the mandatory logical structure for the report? → A: Title → Summary Table → Analytical Insights → Technical/Reproducibility Metadata → References.
- Q: What is the primary output language for the report? → A: Spanish.

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.
  
  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Generate Report Table (Priority: P1)

As an economist, I want to automatically generate a summary table of Banxico's monetary policy meetings for the current year up to the current date, so that I can quickly analyze the relationship between inflation, interest rates, and the exchange rate.

**Why this priority**: This is the core functionality that provides the primary value to the user.

**Independent Test**: Can be tested by running the generator with a valid SIE token and verifying that the output table contains data for past meetings and empty cells for future ones.

**Acceptance Scenarios**:

1. **Given** a valid SIE token and the current year is 2026, **When** I run the report generator on 2026-01-02, **Then** I should see a Markdown table with the dates of the 2026 meetings identified.
2. **Given** a meeting date has passed, **When** the data is fetched, **Then** the corresponding row in the table should be populated with Inflation, Target Rate, and FIX variation.
3. **Given** a meeting date is in the future, **When** the table is generated, **Then** the cells for that date should remain empty as per requirements.

---

### User Story 2 - Analytical Insights and References (Priority: P2)

As a researcher, I want the generated report to include analytical paragraphs and a full list of APA references, so that I can understand the context of the data and verify its sources.

**Why this priority**: Enhances the value of the data by providing context and academic rigor, but depends on the data being available (P1).

**Independent Test**: Verify that the generated Markdown ends with 2-3 analytical paragraphs and a "References" section in APA format.

**Acceptance Scenarios**:

1. **Given** the table is generated, **When** the process finishes, **Then** there should be 2 to 3 paragraphs explaining changes in policy and expectations.
2. **Given** various sources were used (SIE, INEGI, DOF), **When** the references are listed, **Then** they must follow APA format and include the specific URLs and Serie IDs used.

---

[Add more user stories as needed, each with an assigned priority]

### Edge Cases

- **Missing SIE_TOKEN**: The system must exit gracefully or warn the user if the environment variable is not set.
- **Data Not Yet Available**: If a meeting just happened but the SIE series (TI52) hasn't updated, the system must fallback to extracting the rate from the official Policy Statement (PDF/HTML).
- **Broken PDFs**: If the INEGI or Banxico PDF URLs are not found or structured differently, the system should handle the exception without crashing the entire report.
- **Holiday/Non-Business Day FIX**: For `FIX(t-1)`, the system must correctly identify the previous business day based on Banxico's calendar.
- **API Rate Limiting/Errors**: The system must handle HTTP 429 (Too Many Requests) or 5xx errors from the SIE API gracefully.

## Requirements *(mandatory)*

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right functional requirements.
-->

### Functional Requirements

- **FR-001**: System MUST download and parse the official 2026 Monetary Policy Meeting Calendar from Banxico or DOF.
- **FR-002**: System MUST identify meetings that have already occurred (date ≤ today).
- **FR-003**: System MUST fetch annual inflation and core inflation from the latest INEGI INPC bulletin preceding each meeting.
- **FR-004**: System MUST fetch the current inflation target directly from Banxico's official "Objetivo" page or DOF.
- **FR-005**: System MUST fetch the target interest rate from SIE series `TI52`, or fallback to PDF statements if unavailable.
- **FR-006**: System MUST calculate FIX daily variation using SIE series `SF43718` by comparing the rate of the meeting day (`t`) against the rate of the nearest preceding business day (`t-1`) available in the series.
- **FR-007**: System MUST output a Markdown table with specific columns as defined in the goal.
- **FR-008**: System MUST generate 2-3 analytical paragraphs using a deterministic rule-based template engine to ensure data privacy and consistency.
- **FR-009**: System MUST generate a full reference list in APA format, including Serie IDs and URLs.
- **FR-010**: System MUST follow strict data security practices:
    - Never log or store `SIE_TOKEN` in plain text.
    - Use `.env` or environment variables for token management.
    - Ensure `.venv` is used but never read for secrets by the AI agent itself (as per user instruction).
- **FR-011**: System MUST strictly adhere to the [SIE REST API v1 Specification](https://www.banxico.org.mx/SieAPIRest/service/v1/) and [Swagger documentation](https://www.banxico.org.mx/SieAPIRest/service/swagger-ui.html#/Series):
    - Use correct endpoint paths and parameters.
    - Validate response schemas against the API documentation.
    - Include mandatory `Bmx-Token` header in all requests.
- **FR-012**: System MUST include technical design documentation in the `doc/design` directory, covering architecture, data flow, and API integration details.
- **FR-013**: System MUST include user documentation in the `doc/user` directory, providing instructions on how to set up, configure (environment variables), and run the generator.
- **FR-014**: Every function and feature MUST be implemented using Behavior-Driven Development (BDD) methodologies using the `behave` framework.
- **FR-015**: Unit testing MUST achieve at least 80% statement coverage for the entire codebase.
- **FR-016**: The main executable MUST be a command-line interface (CLI) that allows the user to start the report generation process.
- **FR-017**: The CLI MUST be implemented using the `click` Python library.
- **FR-018**: The system MUST mirror the report output to a file in a dedicated `reports/` directory.
- **FR-019**: Persistent report filenames MUST include a precise ISO-8601 compatible timestamp (e.g., `report_2026-01-02T20-00-00.md`) for consistency and ordering.
- **FR-020**: The persistent report file MUST include a section recording the exact Banxico API call(s) used to fetch the data to ensure reproducibility by external tools.
- **FR-021**: All generated content (analytical paragraphs and summaries) MUST maintain a **Formal** tone, similar to an official financial advisor.
- **FR-022**: The language used MUST be **Simple** and accessible, ensuring that individuals without a financial background can understand the insights.
- **FR-023**: The reporting MUST maintain a **Neutral** perspective throughout, avoiding biased or speculative language.
- **FR-024**: The generated report MUST follow a strict logical structure in the following order:
    1.  **Title**: Descriptive title including the current year.
    2.  **Summary Table**: The data table defined in FR-007.
    3.  **Analytical Insights**: Rule-based paragraphs defined in FR-008.
    4.  **Technical Metadata**: Reproducibility data (API calls) defined in FR-020.
    5.  **References**: APA-formatted list defined in FR-009.
- **FR-025**: The entire generated report output (Titles, Table Headers, Analytical Paragraphs, and Reference Sections) MUST be in **Spanish**.

### Key Entities

- **Meeting**: Represents a Banxico Governing Board meeting. Attributes: Date, Status (Past/Future).
- **Inflation Data**: Represents the annual and core inflation rates for a given period.
- **Interest Rate**: Represents the target funding rate.
- **Exchange Rate (FIX)**: Represents the daily exchange rate and its variation.
- **Reference**: Represents a source used for data acquisition. Attributes: Institution, Date, URL, Serie ID (if applicable).

## Success Criteria *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable success criteria.
  These must be technology-agnostic and measurable.
-->

### Measurable Outcomes

- **SC-001**: 100% of past meetings in the current year are included in the report with non-empty data in all required columns (unless data is fundamentally unavailable from official sources).
- **SC-002**: The calculated FIX variation matches the mathematical difference between official SIE values to 4 decimal places.
- **SC-003**: References are complete and strictly follow APA guidelines, enabling third-party verification of every value in the table.
- **SC-004**: The report generation process completes in under 30 seconds (assuming stable internet access to official sources).
