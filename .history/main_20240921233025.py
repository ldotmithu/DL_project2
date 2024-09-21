from mlProject.pipeline.stage_01_data_ingestion import *
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