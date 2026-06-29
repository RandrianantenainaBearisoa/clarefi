from src.core.pipeline.training import refit_model
from src.core.utils.helpers import get_current_model

current_model_id = get_current_model(idOnly=True)
refit_model(current_model_id)