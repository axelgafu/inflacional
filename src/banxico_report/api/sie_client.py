import re
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
        
    def _validate_date_format(self, date_str):
        """Validates that the date string is in YYYY-MM-DD format."""
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
            raise ValueError(f"Date must be in YYYY-MM-DD format, got: {date_str}")

    def get_series_data(self, serie_id, start_date=None, end_date=None):
        """
        Fetches data for a given series and date range.
        Format: /Series/SeriesData/{idSeries}/{fechaInicial}/{fechaFinal}
        """
        url = f"{self.BASE_URL}/series/{serie_id}/datos"
        
        if start_date and end_date:
            self._validate_date_format(start_date)
            self._validate_date_format(end_date)
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
            error_msg = f"HTTP error {response.status_code} fetching series {serie_id}"
            
            # Try to parse Banxico error message if available
            try:
                error_body = response.json()
                if "error" in error_body:
                    error_msg += f": {error_body['error'].get('mensaje', str(error_body['error']))}"
            except Exception:
                pass # Use default http error message if json parse fails
            
            if response.status_code == 429:
                logger.error("Rate limit exceeded (HTTP 429)")
                raise Exception("Banxico API Rate limit exceeded.") from e
            
            logger.error(f"{error_msg}: {e}")
            # Re-raise with the detailed message
            raise Exception(error_msg) from e
            
        except Exception as e:
            logger.error(f"Unexpected error fetching series {serie_id}: {e}")
            raise
