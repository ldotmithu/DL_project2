from mlProject.config.configuration import *
from mlProject import *
import tensorflow as tf 
from tensorflow import keras


class ModelTrain:
    def __init__(self,config:ModelTrainConfig) -> None:
        self.config=config
     
    def train_data(self):
            