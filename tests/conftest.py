import json
import pytest

@pytest.fixture
def make_template_config(tmp_path):
    def _make(config_dict):
        config_path = tmp_path / "template_config.json"
        with open(config_path, "w") as f:
            json.dump(config_dict, f)
        return config_path
    return _make
