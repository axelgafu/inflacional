import pytest
from banxico_report.utils.metadata import MetadataTracker

def test_metadata_tracker_record():
    tracker = MetadataTracker()
    tracker.record_call("http://api.test", params={"id": "1"})
    assert len(tracker.api_calls) == 1
    assert tracker.api_calls[0]["url"] == "http://api.test"

def test_metadata_tracker_generate():
    tracker = MetadataTracker()
    tracker.record_call("http://api.test")
    section = tracker.generate_metadata_section()
    assert "## Datos de Reproducibilidad" in section
    assert "`GET http://api.test`" in section
