from mlProject.entity.config_entity import *
from mlProject.constants import *
from mlProject.utils.common import *
import os


class ConfigurationManager:
    def __init__(self):
        self.config=read_yaml(CONFIG_FILE_PATH)
        self.params=read_yaml(PARAMS_FILE_PATH)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingetsion_config(self):
        config=self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            URL=config.URL,
            locat_data_path=config.locat_data_path,
            unzip_dir=config.unzip_dir
        )    
        return data_ingestion_config
    
    def get_base_model_config(self):
        config=self.config.base_model
        
        
        create_directories([config.root_dir])
        
        base_model_config=BaseModelConfig(
            root_dir=config.root_dir,
            vgg_model=config.vgg_model,
            params_batch_size=self.params.BATCH_SIZE,
            params_classes=self.params.CLASSES,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_image_size=self.params.IMAGE_SIZE,
            params_epchos=self.params.EPOCHS
        )
        return base_model_config
    
    def get_model_train_config(self):
        config=self.config.training
        training_data=os.path.join(self.config.data_ingestion.unzip_dir,'Chest-CT-Scan-data')
        create_directories([Path(config.root_dir)
                            
                            ])
        
        model_train_config=ModelTrainConfig(
            root_dir=config.root_dir,
            vgg_model=config.vgg_model,
            final_model=config.final_model,
            training_data=Path(training_data),
            params_batch_size=self.params.BATCH_SIZE,
            params_classes=self.params.CLASSES,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_image_size=self.params.IMAGE_SIZE,
            params_epchos=self.params.EPOCHS
        )
        
        return model_train_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model="artifacts\training\final_model.h5",
            training_data="artifacts\data_ingestion\Chest-CT-Scan-data",
            mlflow_uri="https://dagshub.com/ldotmithu/DL_project.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config