from src.core.utils.helpers import check_file_presence, get_current_model, get_artifact_store
from src.core.pipeline.model_to_onnx import convert_joblib_to_onnx

current_model = get_current_model()
if (check_file_presence(current_model)):
    print("Starting conversion of current model: joblib to onnx...")
    convert_joblib_to_onnx()
    print("Conversion done.")
else:
    print(f"No current model specified in model_config.yaml or the specified model doesn't exist in '{get_artifact_store()}'")