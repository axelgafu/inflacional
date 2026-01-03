# Research: Banxico Inflation Report Generator

## Decisions

### 1. PDF Parsing Strategy
- **Decision**: Use `pdfplumber`.
- **Rationale**: Best-in-class for extracting structured tables and text layouts from text-based PDFs. Since Banxico and INEGI documents are official and consistent, `pdfplumber` offers the precision needed to extract meeting dates and inflation figures reliably.
- **Alternatives Considered**: 
  - `Camelot`: Excellent for tables but slightly more complex dependencies (Ghostscript).
  - `PyMuPDF (fitz)`: Very fast but lacks the built-in table extraction logic of `pdfplumber`.

### 2. Rule-based Template Engine
- **Decision**: Python's built-in `string.Template` + Logic Helper.
- **Rationale**: Complies strictly with Constitution Principle I (Security & Privacy) by avoiding complex external logic or AI inference. deterministic and 100% private. Simple logic for paragraph selection (e.g., if inflation > target) will be handled in Python code before being passed to the template.
- **Alternatives Considered**: 
  - `Jinja2`: Powerful but potentially overkill and harder to "sandbox" completely for a simple deterministic requirement.

### 3. APA Reference Formatting
- **Decision**: Custom `APAFormatter` implementation.
- **Rationale**: No lightweight Python library perfectly implements APA 7th Edition for Mexican official sources (Banxico/INEGI). A custom implementation ensures 100% accuracy and complete control over the required metadata (URLs, Serie IDs).
- **Alternatives Considered**: 
  - `python-autocite`: Limited support for specific Mexican government formats.

## Risks & Mitigations

- **Risk**: Banxico/INEGI PDF format changes.
- **Mitigation**: Implement robust error handling and fallback to parsing summary HTML if PDF structure fails. Design parsers with modular "selectors" that are easy to update.
