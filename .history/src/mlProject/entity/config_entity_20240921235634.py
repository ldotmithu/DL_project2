from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir:Path
    URL:str
    locat_data_path:Path
    unzip_dir:Path

@dataclass
class BaseModelConfig:
    root_dir:Path
    vgg_model:Path  
    params_image_size:list
    params_target_size:  