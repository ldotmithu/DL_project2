import tensorflow as tf 
from tensorflow import keras
from mlProject.config.configuration import *
from mlProject import logging

class BaseModel:
    def __init__(self,config:BaseModelConfig):
        self.config=config
        #self.params=params
        
        