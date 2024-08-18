from pathlib import Path 
import os 

def find_project_root(starting_dir: Path, marker: str = "config/config.yaml") -> Path:
    current_dir = starting_dir
    while not (current_dir / marker).exists():
        if current_dir.parent == current_dir:
            # If we reach the system root directory without finding the marker
            raise FileNotFoundError(f"Project root with marker '{marker}' not found.")
        current_dir = current_dir.parent

    return current_dir

project_root = find_project_root(Path(os.getcwd()))

# initialize variablest to config.yaml and params.yaml so we don't need to specify the path every time we want to access them
CONFIG_FILE_PATH = project_root / "config/config.yaml"
PARAMS_FILE_PATH = project_root / "params.yaml"
