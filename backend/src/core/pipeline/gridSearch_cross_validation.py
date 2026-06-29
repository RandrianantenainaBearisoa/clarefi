from src.core.utils.helpers import load_config_file, get_grid_search_config, generate_random_string, ask_user_choices, get_artifact_store
from src.core.pipeline.cross_validation_pipeline import custom_pipeline
from src.core.pipeline.data_pipeline import get_train_data, get_test_data
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
import datetime
import traceback
import yaml
import joblib

def store_experiment(gridCV:dict, gridCV_args:dict, pipeline:dict, param_grid:dict, dataset_proportion:float, report:dict):
    params = {param: str(param_grid[param]) for param in param_grid}
    best_params = {param:gridCV.best_params_[param] if (type(gridCV.best_params_[param]).__name__ != "tuple") else str(gridCV.best_params_[param]) for param in gridCV.best_params_ }
    steps = dict(pipeline.steps)
    steps = {key: str(steps[key]) for key in steps}

    model_name = generate_random_string(10)

    data = {
        "model": model_name,
        "experiment_timestamp": datetime.datetime.now(),
        "pipeline": steps,
        "info": {
            "gridCV_args": gridCV_args,
            "param_grid": params,
            "dataset_proportion": dataset_proportion,
            "best_params": best_params,
            "best_score": float(gridCV.best_score_),
            "report": report
        }
    }

    file_path = "config/experiment_result.yaml"

    try:
        with open(file_path , "r") as file:
            existing_data = yaml.safe_load(file) or []
    except FileNotFoundError:
        existing_data = []

    with open(file_path , "w") as file:
        yaml.dump(
            [data] + existing_data,
            file, 
            default_flow_style=False, 
            sort_keys=False
        )
    return model_name

def store_artefact(best_pipeline:Pipeline, model_id:str, forProd:bool = True):
    artifact_path = get_artifact_store() + f"model_{model_id}.joblib"
    joblib.dump(best_pipeline, artifact_path)
    print(f"Model artifact saved at {artifact_path}")
    if forProd:
        set_model_on_prod(artifact_path)
    else:
        if ask_user_choices("Do we use it for inference on prod ?") == "Yes":
            set_model_on_prod(artifact_path)
            print("This model is used for inference on prod.")
        else:
            print("Not used for inference on prod.")

def save_artefact(best_pipeline:Pipeline, model_name:str):
    if ask_user_choices("Read the experiment result on the file experiment_result.yaml\nDo we save the artifact of the best estimator ?") == "Yes":
        store_artefact(best_pipeline=best_pipeline, model_id=model_name)
    else:
        print("Model artifact not saved")

def set_model_on_prod(model_name: str):
    model_config_file_path = "config/model_config.yaml"
    model_config = load_config_file(model_config_file_path)
    model_config["model_on_prod"] = model_name
    with open(model_config_file_path , "w") as file:
        yaml.dump(
            model_config,
            file,
            default_flow_style=False, 
            sort_keys=False
        )
    print(f"Model {model_name} is the new model on prod.")

def run_gs_cross_validation():
    configurations = get_grid_search_config()
    X, y = get_train_data()
    X_test, y_test = get_test_data()

    proportion = round(len(X)*configurations["dataset_proportion"])
    if not (0 <= proportion <= len(X)):
        proportion = 10

    try:
        pipeline = custom_pipeline(configurations["transformers"], configurations["regressor"])
        param_grid = {param: eval(configurations["param_grid"][param]) for param in configurations["param_grid"]}
        
        gridCV = GridSearchCV(
            estimator=pipeline,
            param_grid=param_grid,
            cv=configurations["GridSearchCV"]["cv"],
            n_jobs=configurations["GridSearchCV"]["n_jobs"],
            verbose=configurations["GridSearchCV"]["verbose"]
        )
        gridCV.fit(X[:proportion], y[:proportion])

        y_pred = gridCV.predict(X_test)
        report = classification_report(y_test, y_pred, output_dict=True, target_names=['Negative', 'Positive'])
        
        model_name = store_experiment(gridCV=gridCV, gridCV_args=configurations["GridSearchCV"], pipeline=pipeline, param_grid=param_grid, dataset_proportion=configurations["dataset_proportion"], report=report)
        save_artefact(best_pipeline=gridCV.best_estimator_, model_name=model_name)

    except Exception:
        traceback.print_exc()