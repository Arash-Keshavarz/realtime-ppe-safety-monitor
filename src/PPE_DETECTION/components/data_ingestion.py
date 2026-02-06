import os
import requests
import zipfile
from PPE_DETECTION.entity.config_entity import DataIngestionConfig
from PPE_DETECTION import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        try:
            root_dir = self.config.root_dir
            dataset_url = self.config.source_URL
            zip_download_path = self.config.local_data_file
            unzipped_data_dir = self.config.unzipped_data_dir

            logger.info(f"Starting dataset download from {dataset_url}")

            # Create directories
            os.makedirs(root_dir, exist_ok=True)
            os.makedirs(unzipped_data_dir, exist_ok=True)

            # Download ZIP
            response = requests.get(dataset_url, stream=True)
            response.raise_for_status()

            with open(zip_download_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            logger.info(f"Dataset downloaded to {zip_download_path}")

            # Unzip
            with zipfile.ZipFile(zip_download_path, "r") as zip_ref:
                zip_ref.extractall(unzipped_data_dir)

            logger.info(f"Dataset extracted to {unzipped_data_dir}")

        except Exception as e:
            logger.error(f"Error occurred while downloading dataset: {e}")
            raise e
