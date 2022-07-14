import logging
import sys
import os
import subprocess
from src.config import Configuration
from src.constants import *
from src.exception import CustomException
from src.entity import DummyConfig

logging.basicConfig(
    filename=os.path.join("logs", "running_logs.log"),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a",
)
logger = logging.getLogger(__name__)

class Template:
    def __init__(self, dummy_config_var=DummyConfig):
        logger.info(">>>>>Template CLass<<<<<<")
        self.dummy_config_var = dummy_config_var

    def dummy(self) -> None:
        """
        This is a dummy function.
        Returns: None
        """
        logger.info(">>>>>Installation of detectron2 started<<<<<<")
        try:
            pass
        except Exception as e:
            message = CustomException(e, sys)
            logger.error(message.error_message)
            raise message
        logger.info(">>>>>Installation of detectron2 finished<<<<<<")

if __name__ == "__main__":
    project_config = Configuration()
    obj = Template(project_config.get_dummy_config_var())
    obj.dummy()