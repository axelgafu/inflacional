import json
import pathlib
from src.banxico_report.api.provider import SIEProvider

class MockSIEProvider(SIEProvider):
    """
    Mock implementation of SIEProvider that reads from static JSON files.
    """
    
    def __init__(self, mock_dir=None):
        if mock_dir is None:
            # Default to tests/mocks/sie relative to project root
            self.mock_dir = pathlib.Path(__file__).parent / "sie"
        else:
            self.mock_dir = pathlib.Path(mock_dir)
            
    def get_series_data(self, serie_id: str, start_date: str = None, end_date: str = None) -> dict:
        """
        Reads mock data from a JSON file matching the serie_id.
        """
        file_path = self.mock_dir / f"{serie_id}.json"
        
        if not file_path.exists():
            raise FileNotFoundError(f"Mock data not found for series {serie_id} at {file_path}")
            
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        return data
