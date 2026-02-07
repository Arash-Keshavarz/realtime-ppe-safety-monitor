from PPE_DETECTION.constants import *
from PPE_DETECTION.utils.common import read_yaml, create_directories
from PPE_DETECTION.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig
from pathlib import Path
import os



class ConfigurationManager:
    def __init__(self,
                 config_filepath: Path = CONFIG_FILE_PATH,
                 params_filepath: Path = PARAMS_FILE_PATH):
        
        # Read the yaml files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        # Create the artifacts directory
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzipped_data_dir=Path(config.unzipped_data_dir)
        )
        
        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        params = self.params.training
        
        create_directories([config.root_dir])
        
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            
            # Pass params needed for model setup
            params_image_size = params.img_size,
            params_learning_rate = params.learning_rate,
            params_weights = params.weights,
            params_classes = self.params.data.num_classes
        )
        
        return prepare_base_model_config