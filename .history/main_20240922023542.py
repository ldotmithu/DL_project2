from mlProject.pipeline.stage_01_data_ingestion import *
from mlProject.pipeline.stage_02_base_model import *
from mlProject.pipeline.stage_03_mosel_train import *
from mlProject.pipeline.stage_04_model_evl import *
from mlProject import logging

Stage_name='Data Ingestion'
try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f'{Stage_name} Complated')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(e)
    raise

Stage_name='Prepare Base Model '
try:
    base_model=BaseModelPipeline()
    base_model.main()
    logging.info(f'{Stage_name} Complated')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(e)
    raise


Stage_name='Train Model '
try:
    model_train=ModelTrainPipeline()
    model_train.main()
    logging.info(f'{Stage_name} Complated')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(e)
    raise


Stage_name='Train Model '
try:
    model_evl=EvaluationPipeline()
    model_evl.main()
    logging.info(f'{Stage_name} Complated')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(e)
    raise