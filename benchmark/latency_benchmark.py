
import time
import tensorflow as tf
import numpy as np

def benchmark_model(model_path, input_shape):
    """
    Benchmark the latency of a TensorFlow Lite model.
    Args:
        model_path (str): Path to the TFLite model.
        input_shape (tuple): Input shape for the model.
    Returns:
        dict: Benchmark results with latency and input/output details.
    """
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_data = np.random.random(input_shape).astype(np.float32)

    start_time = time.time()
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    inference_time = time.time() - start_time

    return {
        "latency": inference_time,
        "input_details": input_details,
        "output_details": output_details,
    }
