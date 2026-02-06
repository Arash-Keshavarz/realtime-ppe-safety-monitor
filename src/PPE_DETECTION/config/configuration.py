from PPE_DETECTION.constants import *
from PPE_DETECTION.utils.common import read_yaml, create_directories
from PPE_DETECTION.entity.config_entity import DataIngestionConfig
from pathlib import Path
import os



class ConfigurationManager:
    def __init__(self,
                 config_filepath: Path = CONFIG_FILE_PATH,
                 params_filepath: Path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzipped_data_dir=Path(config.unzipped_data_dir)
        )
        
        return data_ingestion_config

