import os
from datetime import datetime
from .logger import setup_logger

logger = setup_logger(__name__)

def save_report(content, directory="reports"):
    """
    Saves the report content to a file with a timestamped name.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    filename = f"report_{timestamp}.md"
    file_path = os.path.join(directory, filename)
    
    try:
        logger.info(f"Saving report to {file_path}")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return file_path
    except Exception as e:
        logger.error(f"Error saving report to {file_path}: {e}")
        raise
