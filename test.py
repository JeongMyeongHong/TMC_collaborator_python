import torch

import tensorflow as tf
import tensorflow_hub as hub

if __name__ == '__main__':

    print(tf.test.gpu_device_name())

    print(torch.cuda.is_available())  # True

    print("Version: ", tf.__version__)
    print("Eager mode: ", tf.executing_eagerly())
    print("Hub version: ", hub.__version__)
    print("GPU is available" if tf.config.list_physical_devices("GPU") else "NOT AVAILABLE")
