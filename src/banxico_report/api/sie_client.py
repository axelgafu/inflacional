import requests
from ..utils.logger import setup_logger

logger = setup_logger(__name__)

class SIEClient:
    BASE_URL = "https://www.banxico.org.mx/SieAPIRest/service/v1"
    
    def __init__(self, token, tracker=None):
        self.token = token
        self.tracker = tracker
        self.headers = {
            "Bmx-Token": self.token,
            "Accept": "application/json"
        }
        
    def get_series_data(self, serie_id, start_date=None, end_date=None):
        """
        Fetches data for a given series and date range.
        Format: /Series/SeriesData/{idSeries}/{fechaInicial}/{fechaFinal}
        """
        url = f"{self.BASE_URL}/Series/SeriesData/{serie_id}"
        
        if start_date and end_date:
            url += f"/{start_date}/{end_date}"
            
        if self.tracker:
            self.tracker.record_call(url)
            
        try:
            logger.info(f"Fetching data for series {serie_id} from {url}")
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            return data
            
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                logger.error("Rate limit exceeded (HTTP 429)")
                raise Exception("Banxico API Rate limit exceeded.") from e
            logger.error(f"HTTP error fetching series {serie_id}: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error fetching series {serie_id}: {e}")
            raise
