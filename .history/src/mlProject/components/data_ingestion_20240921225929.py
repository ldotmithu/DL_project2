from mlProject.config.configuration import DataIngestionConfig
from mlProject import logging
import urllib.request as request
import os,zipfile

class DataIngestion:
    def __init__(self,config: DataIngestionConfig) -> None:
        self.config=config
        
    def download_file(self):
        try:
            if not os.path.exists(self.config.locat_data_path):
                request.url    
        
