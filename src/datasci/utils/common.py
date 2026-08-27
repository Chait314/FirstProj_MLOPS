import os 
import yaml
from src.datasci import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError;

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    Reads yaml file and returns

    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty files
    
        Returns:
            ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file);
            logger.info(f"yaml file: {path_to_yaml} loaded successful");
            return ConfigBox(content);
    except BoxValueError:
        raise ValueError("yaml is empty");
    except Exception as e:
        raise e;

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create List of Directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs to be created.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok = True);
        if verbose:
            logger.info(f"created directory at: {path}");
    
@ensure_annotations
def save_json(path:Path, data: dict):
    """ 
    save json data
    args:
        path (path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path,'w') as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def save_bin(data:Any, path:Path):
    """
    save binary: file
    args: data (any): data to be saved as binary
    path: path to binary file
    """
    joblib.dump(value=data, filename=path);
    logger.info(f"binary file saved at: {path}");

@ensure_annotations
def load_bin(path: Path)-> Any:
    """
    load binary data
    Args:
        path: path to binary file
    Returns:
        any: objects stored in the file
    """
    data = joblib.load(path);
    logger.info(f"binary file loaded from: {path}");
    return data;