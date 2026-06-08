from datasets import load_dataset
from src.core.utils.helpers import download_hf_dataset
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