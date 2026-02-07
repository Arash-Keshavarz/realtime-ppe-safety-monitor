import os
import shutil
from ultralytics import YOLO
from PPE_DETECTION.entity.config_entity import TrainingConfig
from PPE_DETECTION import logger
import torch


class ModelTrainer:
    def __init__(self, config: TrainingConfig):
        self.config = config
        
    def train(self):
        try:

               
            if torch.cuda.is_available():
                device = "0"
                logger.info("✅ NVIDIA GPU detected. Using device='0'")
            else:
                device = "cpu"
                logger.warning("⚠️ No GPU detected. Using device='cpu' (This will be slow!)")
            # ---------------------------------------------------------
                
            
            logger.info(f"Loading model from {self.config.updated_base_model_path}")
            model = YOLO(self.config.updated_base_model_path)
            
            logger.info("Starting training...")
            model.train(
                data = str(self.config.training_data),
                epochs = self.config.params_epochs,
                batch = self.config.params_batch_size,
                imgsz = self.config.params_image_size,
                augment = self.config.params_is_augmentation,
                project = str(self.config.root_dir),
                name = "yolo_run",
                exist_ok = True,
                device = device
            )
            
            logger.info("Training completed.")
            
            yolo_output_dir = os.path.join(self.config.root_dir, "yolo_run", "weights")
            best_model_path = os.path.join(yolo_output_dir, "best.pt")
            
            if os.path.exists(best_model_path):
                shutil.copy(best_model_path, self.config.trained_model_path)
                logger.info(f"Best model copied to {self.config.trained_model_path}")
            else:
                logger.warning(f"Could not find best.pt in {yolo_output_dir}. Please check the training output.")
            
            
        except Exception as e:
            logger.error(f"Error in loading model: {e}")
            raise e