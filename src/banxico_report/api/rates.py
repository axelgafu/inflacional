from .sie_client import SIEClient
from ..utils.logger import setup_logger

logger = setup_logger(__name__)

class RatesFetcher:
    SERIE_TARGET_RATE = "TI52"
    
    def __init__(self, client: SIEClient):
        self.client = client
        
    def get_target_rate(self, reference_date):
        """
        Fetches the target interest rate for the given date.
        """
        logger.info(f"Fetching target interest rate for {reference_date}")
        
        # In a real implementation, we would call self.client.get_series_data
        
        # Mocking for MVP
        return 10.25
