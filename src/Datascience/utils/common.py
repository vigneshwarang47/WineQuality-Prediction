import os
import yaml
from src.Datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """Reads yaml file and returns

    Args:
        path_to_yaml (str): path like input
    
    Raises:
    ValueError: if yaml file is empty
    e: empty file

    Returns:
        ConfigBox: _description_
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directory:list,verbose=True):
    """Create list of directories

    Args:
        path_to_directory (list): List of path of directories
        verbose (bool, optional): ignore if multiple dirs is to be created. Defaults to True.
    """
    for path in path_to_directory:
        os.makedirs(path,exists=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path,data:dict):
    """Save json data

    Args:
        path (Path): Path to json file
        data (dict): Data to be saved in json file
    """
    
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
        
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """Load json files data

    Args:
        path (Path): Path of the json file

    Returns:
        ConfigBox: Data as class attributes instead of dict
    """
    
    with open(path) as f:
        content= json.load(f)
        
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    """Save binary file

    Args:
        data (Any): Data to be saved as binary
        path (Path): Path to binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path:Path)-> Any:
    """Load the binary data

    Args:
        path (Path): Path to binary file

    Returns:
        Any: Object stored in tbe file
    """
    
    data=joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data