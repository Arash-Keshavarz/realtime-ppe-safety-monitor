import os
try:
    # python-box versions differ in what they expose; guard for lint/runtime robustness
    from box.exceptions import BoxValueError
except Exception:  # pragma: no cover
    BoxValueError = ValueError  # type: ignore[assignment]
import yaml
from PPE_DETECTION import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, Dict
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, encoding="utf-8") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("YAML file loaded successfully: %s", path_to_yaml)
            return ConfigBox(content)
    except BoxValueError as exc:
        raise ValueError("YAML file is empty") from exc
    except Exception as exc:
        raise exc from exc  
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they do not exist.

    Args:
        path_to_directories (List[Path]): List of directory paths to create.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info("Created directory at: %s", path)
            

#@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): The path to the JSON file.
        data (Dict[str, Any]): The data to save.
    """
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info("JSON file saved at: %s", path)
    
    
@ensure_annotations
def load_json(path: Path) -> Dict[str, Any]:
    """Loads a JSON file and returns its contents as a dictionary.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        Dict[str, Any]: The contents of the JSON file as a dictionary.
    """
    with open(path, "r", encoding="utf-8") as json_file:
        content = json.load(json_file)
    logger.info("JSON file loaded from: %s", path)
    
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """Saves data to a binary file using joblib.

    Args:
        data (Any): The data to save.
        path (Path): The path to the binary file.
    """
    joblib.dump(data, path)
    logger.info("Binary file saved at: %s", path)    
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib.

    Args:
        path (Path): The path to the binary file.

    Returns:
        Any: The data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info("Binary file loaded from: %s", path)
    
    return data 

@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in kilobytes (KB).

    Args:
        path (Path): The path to the file.

    Returns:
        str: The size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    logger.info("File size for %s is %s KB", path, size_in_kb)
    return f"{size_in_kb} KB"   

def encodeImageIntoBase64(image_path: Path) -> str:
    """Encodes an image file into a base64 string.

    Args:
        image_path (Path): The path to the image file.

    Returns:
        str: The base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    logger.info("Image encoded into base64: %s", image_path)
    return encoded_string

def decodeBase64ToImage(base64_string: str, output_path: Path) -> None:
    """Decodes a base64 string back into an image file.

    Args:
        base64_string (str): The base64 encoded string of the image.
        output_path (Path): The path to save the decoded image file.
    """
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(base64_string))
    logger.info("Base64 decoded and saved as image: %s", output_path)