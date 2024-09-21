import tensorflow as tf 
from tensorflow import keras
from mlProject.config.configuration import *
from mlProject import logging

class BaseModel:
    def __init__(self,config:BaseModelConfig):
        self.config=config
        #self.params=params
    
    def base_model(self):
        self.vgg_model=tf.keras.applications.VGG16(
            input_shape=self.config.params_image_size,
            include_top=self.config.params_include_top,
            weights=self.config.params_weights
        )
        
        
        for layer in self.vgg_model.layers:
            layer.trainable=False
            
        model=tf.keras.models.Flla    
            
            
                
        