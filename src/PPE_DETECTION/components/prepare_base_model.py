import os
import shutil
from pathlib import Path
from ultralytics import YOLO
from PPE_DETECTION.entity.config_entity import PrepareBaseModelConfig
from PPE_DETECTION import logger

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        try:
            logger.info("Downloading/Loading base model...")
            
            print(f"Attempting to load model from: {self.config.params_weights}")
            model = YOLO(self.config.params_weights) 
            
            downloaded_weight_path = Path(self.config.params_weights) 
            destination_path = self.config.base_model_path

            if not destination_path.exists():
                logger.info(f"Moving base model to {destination_path}")
                shutil.copy(downloaded_weight_path, destination_path)
            else:
                logger.info(f"Base model already exists at {destination_path}")

        except Exception as e:
            logger.error(f"Error in get_base_model: {e}")
            raise e

    def update_base_model(self):

        try:
            source_path = self.config.base_model_path
            target_path = self.config.updated_base_model_path
            
            if not target_path.exists():
                shutil.copy(source_path, target_path)
                logger.info(f"Created updated model copy at {target_path}")
            else:
                logger.info(f"Updated model copy already exists at {target_path}")

        except Exception as e:
            logger.error(f"Error in update_base_model: {e}")
            raise e