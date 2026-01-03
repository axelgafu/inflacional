# User Manual: Banxico Inflation Report Generator

## Setup
1. Install Python 3.10+.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Banxico SIE API Token:
   ```bash
   # Windows
   $env:SIE_TOKEN='your_token_here'
   # Linux/macOS
   export SIE_TOKEN='your_token_here'
   ```

## Usage
Run the generator:
```bash
python -m banxico_report.cli generate
```

## Output
- Console output of the report.
- Markdown file in the `reports/` directory with a timestamped filename.
