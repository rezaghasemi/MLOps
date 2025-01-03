import os
from box import ConfigBox
import yaml
import json
from pathlib import Path
from typing import Any
import json
from mlProject import logger

from ensure import ensure_annotations


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads the YAML file at the given path and returns the contents as a ConfigBox.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox.

    Raises:
        ValueError: If the YAML file is empty.
        yaml.YAMLError: If a YAML parsing error occurs.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except ValueError:
        raise ValueError("yaml file is empty")
    except yaml.YAMLError as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=False):
    """
    Create list of directories.

    Args:
        path_to_directories (list): List of paths to create.
        ignore_log (bool, optional): Ignore if multiple directories is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)    
    logger.info(f"json file saved at: {path}")
    
