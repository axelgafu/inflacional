import pdfplumber
from ..utils.logger import setup_logger

logger = setup_logger(__name__)

def extract_tables_from_pdf(pdf_path):
    """
    Extracts all tables from a PDF file using pdfplumber.
    Returns a list of tables (list of list of strings).
    """
    tables = []
    try:
        logger.info(f"Opening PDF for table extraction: {pdf_path}")
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_tables = page.extract_tables()
                if page_tables:
                    tables.extend(page_tables)
        return tables
    except Exception as e:
        logger.error(f"Error extracting tables from PDF {pdf_path}: {e}")
        raise

def extract_text_from_pdf(pdf_path):
    """
    Extracts all text from a PDF file.
    """
    text = ""
    try:
        logger.info(f"Opening PDF for text extraction: {pdf_path}")
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        logger.error(f"Error extracting text from PDF {pdf_path}: {e}")
        raise
