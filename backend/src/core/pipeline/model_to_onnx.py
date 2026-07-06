import joblib
from skl2onnx import to_onnx
from skl2onnx.common.data_types import StringTensorType
from src.core.utils.helpers import get_current_model, get_onnx_store

def convert_joblib_to_onnx():
    """convert current prod model from joblib to onnx"""
    current_model = joblib.load(get_current_model())
    initial_types = [('text_input', StringTensorType([None, 1]))]
    onnix_model = to_onnx(current_model, initial_types=initial_types)
    with open(f"{get_onnx_store()}current_model.onnx", "wb") as f:
        f.write(onnix_model.SerializeToString())