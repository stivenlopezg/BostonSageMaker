import sys
import logging

# Logger configuration -----------------------------------------------------------------------------------------------

logger = logging.getLogger(name="housing-model")
logger.setLevel(logging.INFO)
consoleHandle = logging.StreamHandler(sys.stdout)
consoleHandle.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
consoleHandle.setFormatter(formatter)
logger.addHandler(consoleHandle)

# AWS ----------------------------------------------------------------------------------------------------------------

AWS_REGION = "us-east-1"

BUCKET = "housing-boston"
KEY = 'boston-data'

LABEL = "medv"

