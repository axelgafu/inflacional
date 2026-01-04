class BanxicoReportError(Exception):
    """Base class for exceptions in this module."""
    pass

class RateRetrievalError(BanxicoReportError):
    """Exception raised when an interest rate cannot be retrieved."""
    pass
