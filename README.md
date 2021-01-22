# Singapore Food Classifier

## Table of Contents

- [Deployment](#deployment)
- [Overview](#overview)
- [Instructions](#Instructions)
- [Information on the Deep Learning model](#Information-on-the-Deep-Learning-model)
- [Authors](#author)

## Deployment
App deployed using docker and flask at https://singapore-food.herokuapp.com/.

![Cover page](img/app-coverpage.png?raw=true "Cover Page")

![Predictions](img/app-prediction.png?raw=true "Prediction")

## Overview
"Singapore Food Classifier" Web APP is a food classifier which can predict your favorite local food with an image of the food you upload. 
It is built based on the REpresentational State Transfer (REST) architecture style. 
The classifier is a trained deep learning prediction model which is able to give a good prediction of 12 local delicacies up to 90% test accuracy! 
List of food include chilli crab, curry puff, dim sum, ice kacang, kaya toast, nasi ayam, popiah, roti prata, sambal stingray, satay, tau huay and wanton noodle.


## Instructions 

- Navigate to https://singapore-food.herokuapp.com/
- Under Image Classifer, upload an image the predicted class will appears


### Information on the Deep Learning model

The model composed of convolutional neural network (CNN). A pre-trained model - Mobilenetv2 with pre-trained weights from Imagenet was utilized as the base model. 
The CNN model is then trained on 1224 food images. Each image is preprocessed into "RGB" mode, size of 224 by 224 and into tensor arrays of shapped (224, 224, 3). 
The images are then batched prior to feeding into the model. 

The model is trained using Adam optimiser using with a learning rate of 0.01 with a learning rate reduction on test accuracy plateau with 20 epoch and early stopping. 

Refer to below for the details of the full model architecture and training dataset.

Architecture of the model consists of the following:

- Input layer 
- Image preprocessing layer
- Base Model: MobileNetv2
- Global Average Pooling Layer
- Dense layer 
- Dropout layer
- Output dense layer

Model training codes can be found in [src/train.py](src/train.py)

## Authors

**[Mengyong Lee](https://www.linkedin.com/in/mylee1/)**


