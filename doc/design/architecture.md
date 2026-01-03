# Architecture: Banxico Inflation Report Generator

## Overview
A Python CLI tool to generate financial reports in Spanish using Banxico and INEGI data.

## Components
- **CLI (`cli.py`)**: Uses `click` for entry point.
- **Generator (`generator.py`)**: Orchestrates data fetching and rendering.
- **Parsers (`parsers/`)**: Handles specialized data extraction (PDF, HTML, Target).
- **API (`api/`)**: Clients for SIE REST API v1.
- **Templates (`templates/`)**: Deterministic rule-based insights.
- **Models (`models/`)**: Data entities.

## Data Flow
1. Fetch 2026 Meeting Calendar.
2. For each past meeting:
   - Fetch Inflation (INEGI).
   - Fetch Target Rate (SIETI52).
   - Fetch FIX Variation (SIESF43718).
3. Render Markdown table.
4. Render Insights using RuleEngine.
5. Record API calls and APA references.
6. Persist to `reports/`.
