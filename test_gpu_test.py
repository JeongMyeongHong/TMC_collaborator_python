# import torch
#
# import tensorflow as tf
# import tensorflow_hub as hub
#
# if __name__ == '__main__':
#
#     print(tf.test.gpu_device_name())
#
#     print(torch.cuda.is_available())  # True
#
#     print("Version: ", tf.__version__)
#     print("Eager mode: ", tf.executing_eagerly())
#     print("Hub version: ", hub.__version__)
#     print("GPU is available" if tf.config.list_physical_devices("GPU") else "NOT AVAILABLE")


import torch
import tensorflow as tf
from tensorflow.python.client import device_lib

if __name__ == '__main__':
    print(torch.__version__)

    print(device_lib.list_local_devices())
    tf.config.list_physical_devices('GPU')

    USE_CUDA = torch.cuda.is_available()
    print(USE_CUDA)

    device = torch.device('cuda:0' if USE_CUDA else 'cpu')
    print('학습을 진행하는 기기:', device)
