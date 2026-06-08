from src.core.utils.helpers import load_config_file, get_data_source_name, get_data_destination

def test_load_config_file():
    data_config = load_config_file("config/data_config.yaml")
    assert data_config["data_destinations"][0]["raw_data"] == "data/data_lake"

def test_get_data_destination():
    assert get_data_destination() == "data/data_lake"

def test_get_data_source_name():
    data_source_name = get_data_source_name()
    assert data_source_name == "tblard/allocine"