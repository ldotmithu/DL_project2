from mlProject.config.configuration import DataIngestionConfig
from mlProject import logging
import urllib.request as request
import os,zipfile

class DataIngestion:
    def __init__(self,config: DataIngestionConfig) -> None:
        self.config=config
        
    def download_file(self):
        try:
            url=self.config.URL
            zip_dir=self.config.locat_data_path
            os.makedirs()    
        
