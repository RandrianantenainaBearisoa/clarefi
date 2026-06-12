from datasets import Dataset, concatenate_datasets, load_from_disk
from src.core.utils.helpers import download_hf_dataset, get_data_destination
import traceback

def run_data_ingestion():
    """
    Runs the data ingestion process by downloading the data sources specified in the config file.
    Args:
        replace (bool = True): whether to replace the file if it already exists in the data lake.
    Returns:
        None
    """
    print("\nStarting Data ingestion ...\n")
    is_succes = True
    
    try:
        download_hf_dataset()
    except Exception:
        is_succes = False
        traceback.print_exc()
    finally:
        message = "Data ingestion done successfully" if is_succes else "An error occured during Data Ingestion step."
        print(f"\n {message} \n")

def train_validation_data_concat(training_set: list[Dataset]):
    """Combine the train data with the validation data from HF to form an unique training_set for cross-validation
    Args: list of Dataset object to concat
    Returns: unique Dataset object
    """
    return concatenate_datasets(training_set, axis=0)
    
def get_train_data():
    raw_data_store = get_data_destination()

    train_data = load_from_disk(raw_data_store)["train"]
    validation_data = load_from_disk(raw_data_store)["validation"]

    dataset = train_validation_data_concat([train_data, validation_data])

    return dataset["review"], dataset["label"]

def get_test_data():
    raw_data_store = get_data_destination()
    test_data = load_from_disk(raw_data_store)["test"]
    return test_data["review"], test_data["label"]