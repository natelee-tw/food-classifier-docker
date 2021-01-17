from ..src.inference import *
import numpy as np
from PIL import Image


def test_resize_and_return_vector():
    arr = np.random.randint(low=0, high=255, size=(300, 300, 3))
    randomly_generated_image = Image.fromarray(arr.astype('uint8'))

    img = resize_and_return_vector(randomly_generated_image)

    assert img.shape == (1, 299, 299, 3)


def test_return_class():
    prediction_prob = np.array([1.0559259e-02, 9.1975722e-05, 2.1499982e-04, 2.1253927e-05,
                        6.3640062e-09, 1.8555684e-04, 6.8941182e-07, 2.3657232e-05,
                        4.5429770e-06, 5.6543523e-03, 4.4471375e-07, 9.8324329e-01])

    class_name = return_class(prediction_prob)
    assert class_name == 'Wanton Noodle'


def test_return_probability():
    prediction_prob = np.array([1.0559259e-02, 9.1975722e-05, 2.1499982e-04, 2.1253927e-05,
                        6.3640062e-09, 1.8555684e-04, 6.8941182e-07, 2.3657232e-05,
                        4.5429770e-06, 5.6543523e-03, 4.4471375e-07, 9.8324329e-01])

    probability = return_probability(prediction_prob)

    assert probability == 0.98