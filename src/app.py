from PIL import Image
import logging
from flask import Flask, jsonify, request, render_template
from .inference import load_models, resize_and_return_vector, predict_image, return_class, return_probability
from io import BytesIO
import re
import base64


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

model = load_models('src/tensorfood.json', 'src/tensorfood.h5')
app.logger.info('model lock and loaded')


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/info', methods=['GET'])
def short_description():
    if request.method == 'GET':
        info = {"model": "InceptionV3",
                "input-size": "299x299x3",
                "num-classes": 12,
                "pretrained-on": "ImageNet"
                }
        return info


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_img = request.json

        image_data = re.sub("^data:image/.+;base64,", "", input_img)
        img = Image.open(BytesIO(base64.b64decode(image_data)))
        img = resize_and_return_vector(img)

        prediction_prob = predict_image(img, model)
        food_class = return_class(prediction_prob)
        proba = round(return_probability(prediction_prob) * 100)
        app.logger.info('predicted %s with %s probability', food_class, proba)
        return {'class': food_class, 'probability': str(proba)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000, use_reloader=True)
    # For production mode, comment the line above and uncomment below
    # serve(app, host="0.0.0.0", port=8000)
