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
                validation_split=0.2,
                rotation_range=30
            )
            
            val_datagen=tf.keras.preprocessing.image.ImageDataGenerator(
                rescale=1/255,
                validation_split=0.2
            )
            
            train_data=train_datagen.flow_from_directory(
                directory=self.config.training_data,
                target_size=(224,224),
                shuffle=True,
                batch_size=self.config.params_batch_size,
                subset='training'
                
                
            )
            
            val_data=val_datagen.flow_from_directory(
                directory=self.config.training_data,
               target_size=(224,224),
                shuffle=False,
                batch_size=self.config.params_batch_size,
                subset='validation'
            )
            
            self.model.fit(
                train_data,validation_data=val_data,
                epochs=self.config.params_epchos,verbose=1
            )
            
            self.model.save(self.config.final_model)
            
try:
    config=ConfigurationManager()
    model_train_config=config.get_model_train_config()
    model_train=ModelTrain(config=model_train_config)
    model_train.train_data()            
except Exception as e:
    logging.exception(e)
    raise            