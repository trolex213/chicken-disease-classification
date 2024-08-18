from pathlib import Path 



# initialize variablest to config.yaml and params.yaml so we don't need to specify the path every time we want to access them
CONFIG_FILE_PATH =  Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

print(CONFIG_FILE_PATH, PARAMS_FILE_PATH)