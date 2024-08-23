import os 
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallbacks 
from cnnClassifier import logger 

STAGE_NAME = "Prepare Callbacks stage"

class PrepareCallbackPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        prepare_callbacks.get_tb_ckpt_callbacks()

if __name__ == "__main__":
    try:
        obj = PrepareCallbackPipeline()
        logger.info(f"Starting stage {STAGE_NAME}.")
        obj.main()
        logger.info(f"Completed stage {STAGE_NAME}")
    except Exception as e:
        logger.exception(e) 
        raise e
    
