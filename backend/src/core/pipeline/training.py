import joblib
from src.core.utils.helpers import check_file_presence, get_artifact_store, load_config_file, is_string_a_tuple
from src.core.pipeline.gridSearch_cross_validation import custom_pipeline, store_artefact
from src.core.pipeline.data_pipeline import get_train_data

# Fit a pipeline with particular params from experiment result

def get_model_config(model_id:str):
    experiments = load_config_file("config/experiment_result.yaml")
    models = [exp["model"] for exp in experiments]
    try:
        position = models.index(model_id)
        config = {
            "pipeline": list(experiments[position]["pipeline"].keys()),
            "params": experiments[position]["info"]["best_params"]
        }
        return config
    except ValueError:
        return {}

def refit_model(model_id:str):
    artefact_store = get_artifact_store()
    artefact_name = f"model_{model_id}.joblib"

    if check_file_presence(dir_path=artefact_store, filename=artefact_name):
        print(f"This model is already in the Artifact store: {artefact_store}\nnamed: {artefact_name}")
    else:
        print("Preparing model training ...")

        configs = get_model_config(model_id=model_id)
        regressor = configs["pipeline"].pop()
        transformers = configs["pipeline"]
        params = configs["params"]
        params = {key:params[key] if not is_string_a_tuple(params[key]) else eval(params[key]) for key in params}

        pipeline = custom_pipeline(transformers=transformers, regressor=regressor, verbose=True)
        pipeline.set_params(**params)

        X, y = get_train_data()

        print("Starting model training ...")
        pipeline.fit(X=X, y=y)
        
        print("Training done")
        store_artefact(best_pipeline=pipeline, model_id=model_id)