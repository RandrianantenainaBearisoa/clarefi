from fastapi import FastAPI
from src.core.inference.inference import Inference
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
inference_service = Inference()

class Item(BaseModel):
    input: str | list

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def root(item: Item):
    return inference_service.predict(item.input)