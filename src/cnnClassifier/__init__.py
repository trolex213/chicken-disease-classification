import os 
import sys 
import logging 

# set up logging 
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs" 
log_filepath = os.path.join(log_dir, "running_logs.log") # full path would be logs/running_logs.log
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath), # write to file logs/running_logs.log
        logging.StreamHandler(sys.stdout) # print to console
    ]
)

logger = logging.getLogger("cnnClassifierLogger")