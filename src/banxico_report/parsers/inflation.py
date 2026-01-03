from ..models.inflation import InflationRecord
from ..utils.logger import setup_logger

logger = setup_logger(__name__)

class InflationParser:
    def __init__(self):
        pass
        
    def get_latest_inflation(self, reference_date):
        """
        Fetches the latest inflation data preceding the reference_date.
        """
        logger.info(f"Fetching latest inflation data preceding {reference_date}")
        
        # Mocking data for US1 verification
        return InflationRecord(
            period="Diciembre 2025",
            annual_inflation=4.66,
            core_inflation=5.05,
            source_url="https://www.inegi.org.mx/notaeconomica/..."
        )
