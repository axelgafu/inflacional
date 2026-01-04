from .provider import SIEProvider
from .sie_client import SIEClient

class RealSIEProvider(SIEProvider):
    """
    Real implementation of SIEProvider that communicates with Banxico SIE API.
    Initially a wrapper around SIEClient.
    """
    
    def __init__(self, token: str = None):
        self.client = SIEClient(token=token)
        
    def get_series_data(self, serie_id: str, start_date: str = None, end_date: str = None) -> dict:
        """
        Fetches data using the SIEClient.
        """
        return self.client.get_series_data(serie_id, start_date, end_date)
