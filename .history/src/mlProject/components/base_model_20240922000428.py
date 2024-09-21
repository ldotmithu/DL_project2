import tensorflow as tf 
from tensorflow import keras
from mlProject.config.configuration import *
from mlProject import logging

class BaseModel:
    def __init__(self,config:BaseModelConfig) -> None:
        self.config=config
        