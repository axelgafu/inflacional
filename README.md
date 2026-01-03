# inflacional 📈

**Professional Inflation Report Generator** | *Empowering Finance Experts with Pythonic Precision*

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🏛️ Overview

**inflacional** is a specialized tool designed to bridge the gap between complex economic data and actionable financial insights. It automates the retrieval, processing, and reporting of inflation indices from the **Banxico SIE API**, providing finance professionals with a robust, reliable, and transparent way to generate inflation reports.

Built with a commitment to **technical excellence**, **security**, and **data integrity**, this project serves as a reference implementation for professional financial software development in Python.

---

## 🚀 Key Features

- **Automated Data Retrieval**: Seamless integration with the [Banxico SIE REST API](https://www.banxico.org.mx/SieAPIRest/service/v1/).
- **Professional CLI**: A high-caliber command-line interface for rapid report generation and automation.
- **Deterministic Reporting**: Precise calculations ensuring consistency across all generated reports.
- **Developer-Centric Design**: Extensive documentation, high test coverage (>80%), and BDD-driven development.
- **Strict Isolation**: Secure handling of API tokens and local environments.

---

## 🛠️ Getting Started

### Prerequisites

- **Python 3.10+**
- A valid **Banxico SIE API Token** (Obtain one at [Banxico Token Request](https://www.banxico.org.mx/SieAPIRest/service/v1/tokenRequest.html))

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/inflacional.git
   cd inflacional
   ```

2. **Setup environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure API Token**:
   Create a `.env` file in the root directory:
   ```text
   SIE_TOKEN=your_secure_token_here
   ```

### Execution

Generate your first report with a single command:
```bash
banxico-report generate
```

---

## 📖 Documentation

The project maintains high standards of transparency through comprehensive documentation:

- **Technical Architecture**: Detailed design and data flows in [doc/design/architecture.md](doc/design/architecture.md).
- **Architecture Decisions**: Traceable technical choices in [doc/design/](doc/design/) (ADRs).
- **User Manual**: Comprehensive guide for execution and configuration in [doc/user/manual.md](doc/user/manual.md).

---

## 🧪 Testing and Quality

We prioritize reliability through rigorous testing:

- **BDD suite**: `behave tests/features`
- **Unit tests**: `pytest tests/unit`
- **Coverage**: `coverage report` (Minimum 80% mandatory)

---

## ⚖️ Governance and Principles

This project is governed by the [inflacional Constitution](.specify/memory/constitution.md), ensuring that every feature adheres to our core principles of **Security**, **Quality**, and **Compliance**.

---

## 🤝 Contributing

We welcome professional contributions. Please ensure your code adheres to our BDD workflow and documentation standards before submitting a pull request.

---

*Disclaimer: This project is an independent tool and is not affiliated with the Bank of Mexico (Banxico).*
