from abc import ABC, abstractmethod

class SIEProvider(ABC):
    """
    Abstract Base Class for Banxico SIE API providers.
    """
    
    @abstractmethod
    def get_series_data(self, serie_id: str, start_date: str = None, end_date: str = None) -> dict:
        """
        Fetches series data from Banxico SIE.
        
        Args:
            serie_id: The ID of the series to fetch (e.g., 'SF43718').
            start_date: Optional start date in YYYY-MM-DD format.
            end_date: Optional end date in YYYY-MM-DD format.
            
        Returns:
            A dictionary containing the API response.
        """
        pass
