import joblib
from src.core.utils.helpers import get_current_model

class Inference:

    def __init__(self):
        self.pipeline = joblib.load(get_current_model())

    def predict(self, input:str|list):
        if isinstance(input, str):
            input = [input]
        prediction = self.pipeline.predict(input)
        return prediction.tolist()
        # if len(prediction) == 1:
        #     if prediction[0] == 0:
        #         return "Négatif"
        #     return "Positif"
        # else:
        #     prediction = ["Positif" if (pred == 1) else "Négatif" for pred in prediction]
        #     return prediction