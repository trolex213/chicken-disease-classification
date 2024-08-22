import os 
import sys 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel 
from cnnClassifier import logger 

STAGE_NAME = "Prepare Base Model stage" 

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == "__main__":
    try:
        obj = PrepareBaseModelPipeline()
        logger.info(f"Starting stage {STAGE_NAME}.")
        obj.main()
        logger.info(f"Completed stage {STAGE_NAME}.")
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    