from mlProject.config.configuration import *
from mlProject import *
import tensorflow as tf 
from tensorflow import keras


class ModelTrain:
    def __init__(self,config:ModelTrainConfig) -> None:
        self.config=config
     
    def train_data(self):
            self.model=tf.keras.models.load_model(self.config.vgg_model)
            
            train_datagen=tf.keras.preprocessing.image.ImageDataGenerator(
                rescale=1/255,
                horizontal_flip=True,
                vertical_flip=True,
                rotation_range=0.2,
                zoom_range=0.2,
                validation_split=0.2
            )