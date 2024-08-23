import os
import sys

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

# Rest of your imports and code
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))


from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline 


STAGE_NAME = "Data Ingestion stage"
try:
    data_ingestion = DataIngestionPipeline()
    logger.info(f"Starting stage {STAGE_NAME}.")
    data_ingestion.main()
    logger.info(f"Completed stage {STAGE_NAME}.")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model stage" 
try:
    prepare_base_model = PrepareBaseModelPipeline()
    logger.info(f"Starting stage {STAGE_NAME}.")
    prepare_base_model.main()
    logger.info(f"Completed stage {STAGE_NAME}.")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Prepare Callbacks stage" 
