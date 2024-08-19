import os
import sys
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)
print(f"Updated Python path: {sys.path}")

# Rest of your imports and code
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    data_ingestion = DataIngestionPipeline()
    logger.info(f"Starting stage {STAGE_NAME}.")
    data_ingestion.main()
    logger.info(f"Completed stage {STAGE_NAME}.")
except Exception as e:
    logger.exception(e)
    raise e