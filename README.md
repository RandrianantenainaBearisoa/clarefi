# ClaReFi

ClaReFi is an end-to-end movie review sentiment classification project. It downloads the French movie review dataset from Hugging Face, trains a text classification pipeline, serves predictions through a FastAPI backend, and exposes a Vue 3 frontend interface.

## What this project contains

- `backend/`
  - FastAPI service for sentiment inference
  - model training and experiment pipeline
  - dataset download and local data lake management
  - Prometheus metrics endpoint
- `frontend/`
  - Vue 3 + TypeScript single-page app
  - review sentiment UI for end users
- `docker-compose.yml`, `docker-compose.dev.yml`, `docker-compose.prod.yml`
  - service definitions for backend and frontend containers
- dataset stored in `backend/data/data_lake`
- model artifacts stored in `backend/models/joblibs`

## Key features

- sentiment classification of movie reviews using a scikit-learn pipeline
- backend metrics exposed on `/metrics`
- model configuration via YAML files
- Hugging Face dataset download using `tblard/allocine`
- a simple Vue 3 frontend that communicates with the backend API

## Tech stack

- Python 3.12
- FastAPI
- scikit-learn
- Vue 3, TypeScript, Vite
- Docker, Docker Compose
- Prometheus

## Data source

The project uses the Hugging Face dataset:

- [`tblard/allocine`]("https://huggingface.co/datasets/tblard/allocine")

The dataset is configured in `backend/config/data_config.yaml` and downloaded to `backend/data/data_lake`.

## Project structure

- `backend/src/api/main.py` — FastAPI app exposing `/predict` and `/metrics`
- `backend/src/core/inference/inference.py` — loads the current joblib pipeline and runs predictions
- `backend/src/core/utils/helpers.py` — frequently used functions
- `backend/src/core/pipeline/data_pipeline.py` — downloads and assembles training/test data
- `backend/src/core/pipeline/training.py` — rebuilds a model from best experiment configs
- `backend/config/model_config.yaml` — artifact store, ONNX store, and production model path
- `backend/config/experiment_result.yaml` — saved experiment metadata and best model parameters
- `frontend/src/` — Vue app, router, components, and stores

## Local setup

### Backend

1. Open a terminal and go to the backend folder:
   ```bash
   cd backend
   ```
2. Run the provided shell script to install dependencies, download the dataset, train the production model, and start the API:
   ```bash
   ./run_full_pipeline.sh
   ```

This script uses `uv` to install dependencies from `pyproject.toml`, then runs:
- `launch_data_pipeline.py`
- `train_prod_model.py`
- `show_best_model.py`
- `uv run uvicorn src.api.main:app --reload`

After the backend starts, the inference API is available at:

- `http://127.0.0.1:8000/predict`
- `http://127.0.0.1:8000/metrics`

### Frontend

1. Open another terminal and go to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies and start the Vite dev server:
   ```bash
   ./install_n_run.sh
   ```

The frontend runs locally on `http://localhost:5173` by default.

## Docker setup

### Development compose

Use `docker-compose.dev.yml` to build and run the backend and frontend in development mode:

```bash
docker compose -f docker-compose.dev.yml up --build
```

### Production compose

The `docker-compose.prod.yml` file is configured to use production images for backend and frontend.

## Training & experimentation

### Download dataset

The dataset is downloaded from Hugging Face to the local raw data destination defined in `backend/config/data_config.yaml`.

### Train production model

`backend/train_prod_model.py` uses the current production model ID from `backend/config/model_config.yaml` and retrains the pipeline if needed.

### Experimentations

The experiments workflow is a simple pipeline:

1. Update the search configuration in `backend/config/gridSearch_config.yaml`.
2. Run the experiment script:
   - `python backend/launch_grid_search.py`
3. Inspect results in `backend/config/experiment_result.yaml`.
4. If the best model should be promoted, it is saved to `backend/models/joblibs/` and the production path is updated in `backend/config/model_config.yaml`.

This keeps experimentation organized as:

- config → run → result log → optional model promotion
