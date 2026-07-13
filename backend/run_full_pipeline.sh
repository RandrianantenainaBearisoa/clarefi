echo -e "Install dependencies..."
uv sync --frozen

echo -e "Dependencies Installed...\nActivating Virtual Env. ..."
source .venv/bin/activate

if [[ -n "$(which python)" ]]; then
    echo -e "Virtual env. activated\n"
    echo -e "Launching Data pipeline ...\n"
    python launch_data_pipeline.py # download the dataset from source
    echo -e "Dataset ready for training \nStart Training ..."
    python train_prod_model.py # train locally the model in production (model_on_prod from model_config.yaml)
    echo -e "The model on prod is now in the artefact store \nYou can begin to do experiments with the grid search_config.yaml && launch_grid_search.py \nThe result of the experiment can be desplayed by the script show_best_model.py (ordered by accuracy) like below"
    python show_best_model.py
    echo -e "Running Fastapi server for local Inference"
    uv run uvicorn src.api.main:app --reload
else
    echo "Virtual env. not activated"
fi
