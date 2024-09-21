from mlProject.entity.config_entity import *
from mlProject.constants import *
from mlProject.utils.common import *


class ConfigurationManager:
    def __init__(self):
        self.config=read_yaml(CONFIG_FILE_PATH)
        self.params=read_yaml(PARAMS_FILE_PATH)
        
        create_directories([self.config.artifacts_root])