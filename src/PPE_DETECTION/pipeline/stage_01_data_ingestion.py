from PPE_DETECTION.config.configuration import ConfigurationManager
from PPE_DETECTION import logger
from PPE_DETECTION.components.data_ingestion import DataIngestion



STAGE = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()







if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>> stage {STAGE} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE} completed <<<<<\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e