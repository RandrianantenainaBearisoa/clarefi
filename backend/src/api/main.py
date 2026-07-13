from fastapi import FastAPI
from src.core.inference.inference import Inference
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import make_asgi_app, Counter, Histogram, Summary
from src.core.utils.helpers import get_words_number


app = FastAPI()
inference_service = Inference()

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

class Item(BaseModel):
    input: str | list

origins = ["http://localhost:5173", "http://localhost:9090"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class_distribution = Counter('class_distribution', 'Distribution of the class : negatives & positives.', ['sentiment'])
confidence_score = Histogram('confidence_score', 'Confidence scores of the model.', buckets = [0.51, 0.55, 0.6, 0.7, 0.8, 0.9, 0.95, 0.97, 0.99])
avg_word_number = Summary('avg_word_number', 'Average number of used for the inputs.')
out_of_vocab_rate = Histogram('out_of_vocab_rate', 'Percentage of word out of the Vocabulary of the current model', buckets = [0.51, 0.55, 0.6, 0.7, 0.8, 0.9, 0.95, 0.97, 0.99])
request_latency = Histogram('request_latency', 'Duration of request Processing')

@app.post("/predict")
@request_latency.time()
async def online_prediction(item: Item):

    prediction, prediction_probability, oov_rate = inference_service.predict(item.input)

    confidence = max(prediction_probability[0][0], prediction_probability[0][1])
    sentiment = "Positive" if prediction[0] == 1 else "Negative"
    word_number = get_words_number(item.input)

    class_distribution.labels(sentiment=sentiment).inc()
    confidence_score.observe(confidence)
    avg_word_number.observe(word_number)
    out_of_vocab_rate.observe(oov_rate)

    return prediction
