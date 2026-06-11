from src.core.utils.helpers import get_grid_search_config, generate_random_string
from src.core.pipeline.cross_validation_pipeline import custom_pipeline
from src.core.pipeline.data_pipeline import get_train_data
from sklearn.model_selection import GridSearchCV
import datetime
import traceback
import yaml

def store_experiment(gridCV, gridCV_args, pipeline, param_grid):
    params = {param: str(param_grid[param]) for param in param_grid}
    best_params = {param:gridCV.best_params_[param] if (type(gridCV.best_params_[param]).__name__ != "tuple") else str(gridCV.best_params_[param]) for param in gridCV.best_params_ }
    steps = dict(pipeline.steps)
    steps = {key: str(steps[key]) for key in steps}

    data = {
        "model": generate_random_string(10),
        "experiment_timestamp": datetime.datetime.now(),
        "pipeline": steps,
        "info": {
            "gridCV_args": gridCV_args,
            "param_grid": params,
            "best_params": best_params,
            "best_score": float(gridCV.best_score_)
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

def run_gs_cross_validation():
    configurations = get_grid_search_config()
    X, y = get_train_data()

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
        store_experiment(gridCV=gridCV, gridCV_args=configurations["GridSearchCV"], pipeline=pipeline, param_grid=param_grid)
    except Exception:
        traceback.print_exc()