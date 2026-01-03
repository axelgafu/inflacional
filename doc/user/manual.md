# User Manual: inflacional

Guide for setup, configuration, and execution of the Banxico Inflation Report Generator.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [Output Formats](#output-formats)
5. [Troubleshooting](#troubleshooting)

## Installation

### Prerequisites
- Python 3.10+
- `pip` (Python package manager)

### Setup
1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The application uses environment variables for configuration. Create a `.env` file in the root directory:

```text
SIE_TOKEN=your_token_here
INFLACIONAL_ENV=production|test
```

- `SIE_TOKEN`: Your personal token from Banxico SIE API.
- `INFLACIONAL_ENV`: Set to `test` to use mock data for verification without hitting the API.

## Usage

The application provides a CLI interface powered by `click`.

### Generate Report
To generate the latest inflation report:
```bash
banxico-report generate
```

This command will:
1. Fetch the latest CPI (INPC) data from Banxico.
2. Calculate the annual and monthly inflation rates.
3. Save the report to the local filesystem.

## Output Formats

Reports are saved in the `reports/` directory as Markdown files. The content is also printed to the console for immediate review.

## Troubleshooting

### Missing Token
If you get a `ValueError: Missing SIE_TOKEN`, ensure your `.env` file is present and contains the correct key.

### API Downtime
If the Banxico API is unreachable, the application will provide a graceful error message. You can use `INFLACIONAL_ENV=test` to verify local logic in the meantime.
