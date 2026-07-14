import joblib
from src.core.utils.helpers import get_current_model

class Inference:

    def __init__(self):
        self.pipeline = joblib.load(get_current_model())

        self.vectorizer = self.pipeline.named_steps["countvectorizer"]
        vocab = self.vectorizer.get_feature_names_out()
        
        self.vocab_set = set(vocab)

    def predict(self, input:str|list):
        if isinstance(input, str):
            input = [input]

        prediction = self.pipeline.predict(input)
        prediction_probability = self.pipeline.predict_proba(input)
        oov_rate = self.out_of_vocab_rate(input=input)

        return prediction.tolist(), prediction_probability, oov_rate
    
    def out_of_vocab_rate(self, input:str|list):
        if isinstance(input, str):
            input = [input]
        
        tokens_count = 0
        oov_count = 0

        for text in input:
            tokens_list = self.vectorizer.build_tokenizer()(text)
            tokens_count += len(tokens_list)
            
            for token in tokens_list:
                if token not in self.vocab_set:
                    oov_count += 1
        
        return (oov_count / tokens_count) * 100 if tokens_count else 0.0