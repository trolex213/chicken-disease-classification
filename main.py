import os 
import sys 

# add "src" to the system path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from cnnClassifier import logger 

logger.info("Logger initialized.") # this will write to logs/running_logs.log and print to console

