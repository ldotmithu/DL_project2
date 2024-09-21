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
            
        model=tf.keras.layers.Flatten()(self.vgg_model.output)
        predict_layer=tf.keras.layers.Dense(units=self.config.params_classes,activation='softmax')(model)
        
        model=tf.keras.models.Model(inputs=self.vgg_model.input,outputs=predict_layer) 
        
        model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
        model.summary() 
        
        model.save(self.config.vgg_model)
        
        return model
'''    
try:
    config=ConfigurationManager()
    base_model_config=config.get_base_model_config()
    base_model=BaseModel(config=base_model_config)
    base_model.base_model()   
except Exception as e:
    logging.exception(e)
    raise   
'''               
          
        
                
            
            
                
        