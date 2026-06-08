from datasets import load_dataset
from pathlib import Path
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[3]

def load_config_file(filename: str) -> dict:
    """
    Load the yaml file from the project root.
    Args:
        filename (str): Name of the yaml file to load
    Returns:
        dict: dictionary containing the informations in the yaml file
    Raises:
        FileNotFoundError: if the specified yaml file is not found in the config folder
    """
    config_path = PROJECT_ROOT / filename
    
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found in : {config_path}")
        
    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def get_data_source_name():
    """
    Get the name of the HF data source (for downloads)
    Returns:
        str: the name of the data source in HF
    """
    return load_config_file("config/data_config.yaml")["data_sources"][0]["name"]

def get_data_destination():
    """
    Return the destination folder for unprocessed dataset
    Returns:
        str: relative path to the destination folder
    """
    return load_config_file("config/data_config.yaml")["data_destinations"][0]["raw_data"]

def download_hf_dataset():
    """
    load the dataset from Hugging Face and download it to local storage for raw data
    """
    data_source_name = get_data_source_name()
    raw_train_data_destination = get_data_destination()

    dataset = load_dataset(data_source_name)
    dataset.save_to_disk(raw_train_data_destination)