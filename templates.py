import os 
from pathlib import Path 
import logging 

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# project name
project_name = "cnnClassifier"

# initialize project directories and files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", 
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml", 
    "params.yaml",
    "requirements.txt",
    "setup.py", 
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created: {filedir} for the file {filename}")

    # if the file doesn't exist OR it is an empty file 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            logging.info(f"Empty file created: {filepath}")

    # if file exists and is not an empty file 
    else:
        logging.info(f"{filepath} already exists.")
    