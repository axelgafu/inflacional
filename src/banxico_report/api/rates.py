from datetime import datetime, timedelta
from .provider import SIEProvider
from ..utils.logger import setup_logger
from ..utils.errors import RateRetrievalError
from ..utils.config import get_lookback_window

logger = setup_logger(__name__)

class RatesFetcher:
    SERIE_TARGET_RATE = "TI52"
    
    def __init__(self, provider: SIEProvider, lookback_window: int = None):
        self.provider = provider
        self.lookback_window = lookback_window if lookback_window is not None else get_lookback_window()
        
    def get_target_rate(self, reference_date):
        """
        Fetches the target interest rate for the given date, with look-back logic.
        """
        if isinstance(reference_date, str):
            ref_dt = datetime.strptime(reference_date, "%Y-%m-%d")
        else:
            # Assume it's already a date/datetime object
            ref_dt = reference_date
            
        start_dt = ref_dt - timedelta(days=self.lookback_window)
        
        start_str = start_dt.strftime("%Y-%m-%d")
        end_str = ref_dt.strftime("%Y-%m-%d")
        
        logger.info(f"Fetching target interest rate range: {start_str} to {end_str}")
        
        data = self.provider.get_series_data(self.SERIE_TARGET_RATE, start_date=start_str, end_date=end_str)
        
        try:
            series = data["bmx"]["series"][0]
            if "datos" not in series or not series["datos"]:
                raise RateRetrievalError(
                    f"No interest rate data found for series {self.SERIE_TARGET_RATE} "
                    f"in the window {start_str} to {end_str}"
                )
                
            # Select the latest available observation (last item in the list)
            # Banxico SIE typically returns data in chronological order.
            latest_observation = series["datos"][-1]
            rate_str = latest_observation["dato"]
            observation_date = latest_observation["fecha"]
            
            logger.info(f"Found rate {rate_str} for date {observation_date}")
            return float(rate_str)
            
        except (KeyError, IndexError, ValueError) as e:
            logger.error(f"Error parsing rate data: {e}")
            raise RateRetrievalError(f"Failed to parse interest rate data: {e}")
