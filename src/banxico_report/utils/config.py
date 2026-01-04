import os
from dotenv import load_dotenv

def load_config():
    """Load environment variables from .env file."""
    load_dotenv()
    
    config = {
        "SIE_TOKEN": os.getenv("SIE_TOKEN"),
        # Add other config as needed
    }
    
    return config

def get_token():
    """Returns the SIE_TOKEN or raises error if missing."""
    token = os.getenv("SIE_TOKEN")
    if not token:
        # In a real app we might want a more specific exception
        raise ValueError("Missing SIE_TOKEN environment variable. Please check your .env file.")
    return token
def get_lookback_window():
    """Returns the lookback window for interest rates (default 7 days)."""
    return int(os.getenv("INFLACIONAL_RATES_LOOKBACK", 7))
