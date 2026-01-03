from .sie_client import SIEClient
from ..utils.logger import setup_logger

logger = setup_logger(__name__)

def calculate_fix_variation(current_fix, previous_fix):
    """
    Calculates the daily variation of the FIX exchange rate.
    Standard: current - previous. Rounded to 4 decimals.
    """
    variation = float(current_fix) - float(previous_fix)
    return round(variation, 4)

class ExchangeRateFetcher:
    SERIE_ID = "SF43718"
    
    def __init__(self, client: SIEClient):
        self.client = client
        
    def get_fix_variation(self, meeting_date):
        """
        Fetches the FIX rate for the meeting date (t) and the 
        nearest preceding business day (t-1).
        """
        # Logic to fetch data from SIE API
        # Since we need t and t-1, we might need to fetch a range or 
        # specifically two dates.
        # Requirement: use nearest preceding business day found in SIE series.
        
        # In a real implementation, we would call self.client.get_series_data
        # and process the response to find the correct two dates.
        # For now, this is the skeleton.
        
        # Mock logic for MVP testing
        return 0.0500 
