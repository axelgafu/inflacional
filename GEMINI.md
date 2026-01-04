# inflacional Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-01-02

## Active Technologies
- Python 3.10+ + NyGard ADR Template (Markdown) (003-documentation-standards)
- File-based Markdown in `doc/design/`, `doc/design/adr/`, and `doc/user/`. (003-documentation-standards)
- Python 3.10+ + `requests`, `python-dotenv`, `click`, `behave` (004-api-mock-separation)
- Static JSON files for mock data (residing in `tests/mocks/`) (004-api-mock-separation)
- N/A (API-driven) (005-banxico-api-rates)

- Python 3.10+ + `click`, `behave`, `requests`, `python-dotenv`, `pytest`, `coverage`, `pdfplumber`, `beautifulsoup4` (001-banxico-report)

## Project Structure

```text
src/
tests/
```

## Commands

cd src; pytest; ruff check .

## Code Style

Python 3.10+: Follow standard conventions

## Recent Changes
- 006-fix-banxico-compliance: Added Python 3.10+ + `requests`, `python-dotenv`
- 005-banxico-api-rates: Added Python 3.10+ + `click`, `behave`, `requests`, `python-dotenv`
- 004-api-mock-separation: Added Python 3.10+ + `requests`, `python-dotenv`, `click`, `behave`


<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
