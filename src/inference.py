import sys
import tensorflow as tf
import numpy as np
from PIL import Image


def load_models(json, h5):
    ''' load the h5 and json file and return the model'''
    json_file = open(json, 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    loaded_model = tf.keras.models.model_from_json(loaded_model_json)

    loaded_model.load_weights(h5)
    return loaded_model


def resize_and_return_vector(file):
    ''' resize image to (299, 299) and convert image to array'''
    img = file.resize((224, 224))
    img = np.divide(tf.keras.preprocessing.image.img_to_array(img),255) #convert to vector
    img = np.expand_dims(img, axis=0)
    return img


def predict_image(img, model):
    ''' predict the model class and return prediction probability vector'''
    prediction_prob = model.predict(img)
    return prediction_prob


def return_class(prediction_prob):
    foods = ['Chilli Crab',
             'Curry Puff',
             'Dim Sum',
             'Ice Kacang',
             'Kaya Toast',
             'Nasi Ayam',
             'Popiah',
             'Roti Prata',
             'Sambal Stingray',
             'Satay',
             'Tau Huay',
             'Wanton Noodle']

    class_name = foods[np.argmax(prediction_prob)]
    return class_name


def return_probability(prediction_prob):
    probability = np.max(prediction_prob)
    return np.round(probability, 2)


if __name__ == '__main__':
    file_path = sys.argv[1]

    model = load_models('src/tensorfood.json', 'src/tensorfood.h5')

    img = Image.open(file_path).convert("RGB")

    img = resize_and_return_vector(img)
    prediction_prob = predict_image(img, model)
    class_name = return_class(prediction_prob)
    probability = return_probability(prediction_prob)

    print({class_name, probability})
