import tensorflow as tf
import numpy as np
from keras.preprocessing.image import ImageDataGenerator  # 이미지 전처리를 위한 모듈
from keras.preprocessing import image
from keras.models import load_model


class Cnn:
    def __init__(self, train_path, test_path, num_class, img_size=64, batch_size=16, epochs=10):
        self.train_path = train_path
        self.test_path = test_path
        self.num_class = num_class
        self.img_size = img_size
        self.batch_size = batch_size
        self.epochs = epochs

    def generate_dataset(self):
        train_datagen = ImageDataGenerator(rescale=1. / 255, shear_range=0.2,
                                           zoom_range=0.2, horizontal_flip=True)
        training_set = train_datagen.flow_from_directory(self.train_path,
                                                         target_size=(self.img_size, self.img_size),
                                                         batch_size=self.batch_size,
                                                         class_mode='binary' if self.num_class == 2 else 'categorical')

        validation_datagen = ImageDataGenerator(rescale=1. / 255)
        validation_set = validation_datagen.flow_from_directory(self.test_path,
                                                                target_size=(self.img_size, self.img_size),
                                                                batch_size=self.batch_size,
                                                                class_mode='binary' if self.num_class == 2 else 'categorical')
        print(training_set.class_indices)
        return training_set, validation_set

    def create_model(self):
        return tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu',
                                   input_shape=[self.img_size, self.img_size, 3]),
            tf.keras.layers.MaxPool2D(pool_size=2, strides=2),
            tf.keras.layers.Conv2D(32, 3, activation='relu'),
            tf.keras.layers.MaxPool2D(2, 2),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Conv2D(32, 3, activation='relu'),
            tf.keras.layers.MaxPool2D(2, 2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(units=128, activation='relu'),
            tf.keras.layers.Dropout(rate=0.2),
            tf.keras.layers.Dense(1 if self.num_class == 2 else self.num_class,
                                  activation='sigmoid' if self.num_class == 2 else 'softmax')])

    def fit_model(self):
        model = self.create_model()
        training_set, validation_data = self.generate_dataset()
        model.compile(optimizer='adam',
                      loss='binary_crossentropy' if self.num_class == 2 else 'categorical_crossentropy',
                      metrics=['accuracy'])
        model.fit(x=training_set, validation_data=validation_data, epochs=self.epochs)
        model.save('./save/my_model.h5')

    def classify_image(self, image_path, model):
        test_image = image.load_img(image_path,
                                    target_size=(self.img_size, self.img_size))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image)[0])
        print(np.argmax(model.predict(test_image)[0]))
        if result == 0:
            prediction = 'Rice'
        elif result == 1:
            prediction = 'RoastedFish'
        else:
            prediction = 'RolledOmelet'
        return prediction


if __name__ == '__main__':
    train_path = './data/3images/train'
    test_path = './data/3images/validation'
    model = Cnn(train_path=train_path, test_path=test_path,
                num_class=3, img_size=64, batch_size=8, epochs=10)
    detect_image_path = './data/rice.jpg'
    # model.fit_model()
    print(model.classify_image(detect_image_path, load_model('./save/my_model.h5')))
    my_model = load_model('./save/my_model.h5')
    print(my_model.summary())

