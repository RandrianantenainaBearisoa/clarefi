from datasets import Dataset, Column
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
import traceback

def custom_pipeline(transformers:list = [], regressor:str = 'logisticregression', verbose:bool = False):
    transformers_list = {
        "countvectorizer": CountVectorizer
    }
    regressors_list = {
        "logisticregression": LogisticRegression
    }
    try:
        selected_transformers = [(key, transformers_list[key]()) for key in transformers]
        selected_regressor = [(regressor, regressors_list[regressor]())]
        
        return Pipeline(selected_transformers+selected_regressor, verbose=verbose)
    except KeyError:
        print("Error: the key you used to select transformers or regressor is not in the predefined list\nUse key in the dictionaries or create a new object for your key in the dictionnaries")
        traceback.print_exc()
    except Exception:
        traceback.print_exc()