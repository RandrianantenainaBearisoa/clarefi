from fastapi import FastAPI
from src.core.inference.inference import Inference
from pydantic import BaseModel

app = FastAPI()
inference_service = Inference()

class Item(BaseModel):
    input: str | list

@app.post("/predict")
async def root(item: Item):
    return inference_service.predict(item.input)