import os
import subprocess
import json
import pytest

TEMPLATE_NAME = 'default_app_w_warehouse'
TEMPLATE_PATH = os.path.abspath(f'apps/{TEMPLATE_NAME}')
RENDERED_PROJECT_NAME = 'test_data_app_bundle'

EXPECTED_FILES = [
    f'{RENDERED_PROJECT_NAME}/databricks.yml',
    f'{RENDERED_PROJECT_NAME}/app/app.py',
    f'{RENDERED_PROJECT_NAME}/app/app.yaml',
    f'{RENDERED_PROJECT_NAME}/app/requirements.txt',
    f'{RENDERED_PROJECT_NAME}/resources/data.app.yml'
]
DAB_CLI_CMD = [
    'databricks', 'bundle', 'init',
    TEMPLATE_PATH
]


# Shared fixture to render the template once for all checks
@pytest.fixture(scope="module")
def rendered_template(tmp_path_factory):
    tmp_path = tmp_path_factory.mktemp("dab_template")
    config = {
        "project_name": RENDERED_PROJECT_NAME,
        "app_name": "test-data-app",
        "sql_warehouse_id": "test_warehouse_id"
    }
    config_path = tmp_path / "template_config.json"
    with open(config_path, "w") as f:
        json.dump(config, f)
    cmd = DAB_CLI_CMD + ["--output-dir", str(tmp_path), "--config-file", str(config_path)]
    print(f'Running: {" ".join(cmd)}')
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        assert result.returncode == 0, (
            f"Template render failed!\n"
            f"Exit code: {result.returncode}\n"
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}"
        )
    except Exception as e:
        pytest.fail(f"Error running CLI command: {e}")
    return tmp_path

@pytest.mark.integration
@pytest.mark.parametrize("rel_path", EXPECTED_FILES)
def test_expected_files_exist(rendered_template, rel_path):
    abs_path = rendered_template / rel_path
    assert abs_path.is_file(), f"Missing file: {abs_path}"

@pytest.mark.integration
def test_project_name_in_databricks_yml(rendered_template):
    databricks_yml = rendered_template / f'{RENDERED_PROJECT_NAME}/databricks.yml'
    with open(databricks_yml) as f:
        content = f.read()
        assert RENDERED_PROJECT_NAME in content, "Project name not rendered in databricks.yml"
