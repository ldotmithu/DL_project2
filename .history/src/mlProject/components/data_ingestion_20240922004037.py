from mlProject.config.configuration import DataIngestionConfig
from mlProject import logging
import urllib.request as request
import os,zipfile
import gdown
from mlProject.config.configuration import *
class DataIngestion:
    def __init__(self,config: DataIngestionConfig) -> None:
        self.config=config
        
    def download_file(self):
        try:
            url=self.config.URL
            zip_dir=self.config.locat_data_path
            os.makedirs(self.config.root_dir,exist_ok= True)    
            
            id=url.split('/')[-2]
            prefix= 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+id,zip_dir)
            logging.info('Download Zip data')
            
        except Exception as e:
            logging.exception(e)
            raise e
        
    def Extract_all(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.locat_data_path,'r') as f:
            f.extractall(unzip_path)
            logging.info('Extract All files')   
            
'''                          
try:
    config=ConfigurationManager()
    data_ingestion_config=config.get_data_ingetsion_config()
    data_ingestion=DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.Extract_all()
except Exception as e:
    logging.exception(e)
    raise    
'''     