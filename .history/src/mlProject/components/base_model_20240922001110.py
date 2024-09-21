import tensorflow as tf 
from tensorflow import keras
from mlProject.config.configuration import *
from mlProject import logging

class BaseModel:
    def __init__(self,config:BaseModelConfig):
        self.config=config
        #self.params=params
    
    def base_model(self):
        self.model=tf.keras.applications.VGG16(
            input_shape=self.config.params_image_size,
            inc
        )
            
        