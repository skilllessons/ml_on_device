
import tensorflow as tf

def to_tflite(model_path, quantization=False):
    """
    Convert a TensorFlow model to TensorFlow Lite format.
    Args:
        model_path (str): Path to the TensorFlow model (.h5).
        quantization (bool): Apply quantization for optimization.
    Returns:
        str: Path to the converted TFLite model.
    """
    model = tf.keras.models.load_model(model_path)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    if quantization:
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_model = converter.convert()
    tflite_model_path = model_path.replace(".h5", ".tflite")
    with open(tflite_model_path, "wb") as f:
        f.write(tflite_model)
    return tflite_model_path
