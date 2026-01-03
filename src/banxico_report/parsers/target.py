from ..utils.logger import setup_logger

logger = setup_logger(__name__)

class TargetFetcher:
    def __init__(self):
        pass
        
    def get_inflation_target(self):
        """
        Returns the official inflation target.
        Requirement: Fetch from Banxico page, but for now 3.0 +/- 1pp.
        """
        logger.info("Fetching official inflation target")
        return "3.0% ± 1 pp"
