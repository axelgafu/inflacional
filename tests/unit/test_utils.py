import os
from banxico_report.utils.persistence import save_report
from banxico_report.utils.config import load_config, get_token

def test_save_report(tmp_path):
    report_dir = tmp_path / "reports"
    path = save_report("test content", directory=str(report_dir))
    assert os.path.exists(path)
    with open(path, "r") as f:
        assert f.read() == "test content"

def test_config_load():
    os.environ["SIE_TOKEN"] = "test"
    config = load_config()
    assert config["SIE_TOKEN"] == "test"
    assert get_token() == "test"
