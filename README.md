# Dataset of Images of Dogs, Books, Ducks, Cats, and Aeroplanes

created my own dataset contains images of dogs, books, ducks, cats, and aeroplanes scraped from Google Images.

## Description
The dataset consists of images collected using a web scraping script written in Python. The script uses the Selenium library to automate the process of downloading images from Google Images. The images are categorized into five classes: dogs, books, ducks, cats, and aeroplanes.

## Dataset Information
- Total number of images: {445}
- Categories: Dogs, Books, Ducks, Cats, Aeroplanes
- Image file format: JPG

## Dataset Structure
The dataset is organized into separate folders for each category. The folder structure is as follows as in datavgg

# Image Classification using VGG16
This project is an example of image classification using the VGG16 deep learning architecture. The dataset used for this task contains images of five classes: "Dog", "Elephant", "Flower", "Horse", and "Human". The task is to classify the images into these categories .

## Environment Setup
Python: 3.6 or above
TensorFlow: 2.0 or above
Keras: 2.3.1 or above
NumPy: 1.16.5 or above
Matplotlib: 3.1.1 or above


## Code Overview
Model Architecture: VGG16 pre-trained model is used as a base for feature extraction. The model is loaded with pre-trained ImageNet weights and the last layer (softmax) is modified to output predictions for our five classes.

Model Compilation: The model is compiled using the SGD (Stochastic Gradient Descent) optimizer with a learning rate of 0.01 and momentum of 0.9. The loss function is set to "binary_crossentropy" since this is a multi-label classification problem. The accuracy metric is used to monitor the model's performance.

Data Augmentation: Both the training and testing data generators use the ImageDataGenerator class for data augmentation. Augmentation techniques like rotation, width shift, height shift, shear, zoom, and horizontal flip are applied.

Data Flow: The code establishes data flow using the flow_from_directory() method. It sets up the train and test data generators with target size of (224, 224) and batch size of 32.

Training: The model is trained using model.fit_generator(). It is trained for 10 epochs with 5 steps per epoch and 32 validation steps.

Prediction: A sample image is loaded, preprocessed, and passed to the model for prediction. The output probabilities for each class are printed.
