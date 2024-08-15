# this script defines common utility functions for the CNN classifier so there's no need to define them in every script that uses them
import os 
from box.exceptions import BoxValueError 
import yaml
from cnnClassifier import logger 
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox 
from pathlib import Path 
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''
    reads a yaml file and returns a ConfigBox object with the content of the yaml file

    Args: 
    path_to_yaml: Path -> the path to the yaml file, specified as a Path object 

    '''
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successully read the yaml file at {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Error reading the yaml file at {path_to_yaml}")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    '''
    creates list of directories 

    Args: 
    path_to_directories: list -> a list of paths to directories 
    verbose: bool -> whether to log the creation of the directories or not (in this case set to True, so we do)
    '''
    for path in path_to_directories:
        os.makedir(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    '''
    writes the data inside a dictionary to a json file (same as "saving" the json file)
    '''
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"Saved json file at {path}")


@ensure_annotations
def load_json(path: Path) -> dict:
    '''
    loads content of a json file into a dictionary, wraps the dictionary in a ConfigBox, and returns it. 
    '''
    with open(path, 'r') as json_file:
        content = json.load(json_file)
    logger.info(f"Loaded json file at {path}")
    return ConfigBox(content)


@ensure_annotations 
def save_bins(path: Path, data: Any):
    '''
    writes the data to a binary file (same as "saving" the binary file)
    '''
    joblib.dump(value=data, filename=path) 
    logger.info(f"Saved binary file at {path}")

@ensure_annotations
def load_bins(path: Path, data: Any):
    '''
    loads the content of a binary file and returns it
    '''
    data = joblib.load(filename=path)
    logger.info(f"Loaded binary file at {path}")
    return data 

@ensure_annotations
def get_size(path: Path) -> str: 
    '''
    gets size of the file at the specified path and returns it in KB. 
    1 Kb = 1024 byte

    Args: 
    path: Path -> the path to the file whose size we want to get 
    '''
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"~{size_in_kb} KB" 

def decodeImage(imgstring, fileName):
    '''
    takes a Base64-encoded string representing an image, decode it back into its binary form, and save it as an image file

    Args:
    imgstring -> base64-encoded string representation of an image 
    '''
    imgdata = base64.b64decode(imgstring)
    with open(fileName, "wb") as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    
    
    
    





