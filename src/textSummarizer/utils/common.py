import os
import sys
import yaml
from src.textSummarizer.logging import logger
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from pathlib import Path
from typing import Any


@ensure_annotations
def load_yaml(yaml_path: Path) -> ConfigBox:

    """reads yaml file and returns

    Args:
        yaml_path (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(yaml_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {yaml_path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
