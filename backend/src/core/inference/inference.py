import joblib
from src.core.utils.helpers import get_current_model, get_words_number, get_word_list

class Inference:

    def __init__(self):
        self.pipeline = joblib.load(get_current_model())

        vectorizer = self.pipeline.named_steps["countvectorizer"]
        vocab = vectorizer.get_feature_names_out()
        
        self.vocab_set = set(vocab)

    def predict(self, input:str|list):
        if isinstance(input, str):
            input = [input]

        prediction = self.pipeline.predict(input)
        prediction_probability = self.pipeline.predict_proba(input)
        oov_rate = self.out_of_vocab_rate(input=input)

        return prediction.tolist(), prediction_probability, oov_rate
    
    def out_of_vocab_rate(self, input:str|list):
        if not input:
            return 0.0
        words_list = get_word_list(sentence=input)
        oov_nb = sum(1 for word in words_list if word not in self.vocab_set)
        words_number = get_words_number(input)

        return (oov_nb / words_number) * 100