# Quickstart: Banxico Inflation Report Generator

## Setup

1.  **Environment**: Ensure Python 3.10+ is installed.
2.  **Clone & Install**:
    ```bash
    git clone <repo-url>
    cd inflacional
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # Linux/macOS
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Authentication**:
    Set your Banxico SIE API Token in a `.env` file:
    ```env
    SIE_TOKEN=your_token_here
    ```

## Execution

Generate the latest inflation report:
```bash
python -m banxico_report generate
```

The report will be printed to stdout and saved in the `reports/` directory with a timestamped filename.

## Verification

Run the test suite to ensure everything is working correctly:
```bash
# Run BDD Features
behave tests/features

# Run Unit Tests with Coverage
pytest --cov=src/banxico_report tests/unit
```
