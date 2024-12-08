
import torch

def quantize_model(model_path, framework="pytorch"):
    """
    Apply quantization to a PyTorch model.
    Args:
        model_path (str): Path to the PyTorch model (.pth).
        framework (str): Framework of the model ('pytorch').
    Returns:
        str: Path to the quantized model.
    """
    if framework == "pytorch":
        model = torch.load(model_path)
        model.eval()
        quantized_model = torch.quantization.quantize_dynamic(
            model, {torch.nn.Linear}, dtype=torch.qint8
        )
        quantized_model_path = model_path.replace(".pth", "_quantized.pth")
        torch.save(quantized_model, quantized_model_path)
        return quantized_model_path
    else:
        raise ValueError("Unsupported framework for quantization.")
