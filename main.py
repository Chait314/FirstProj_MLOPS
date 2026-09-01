from src.datasci import logger
from src.datasci.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datasci.pipeline.data_validation import DataValidationPipeline
from src.datasci.pipeline.data_transformation import DataTransformationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<");
    obj = DataIngestionTrainingPipeline();
    obj.initiate_data_ingestion();
    logger.info(f">>> stage {STAGE_NAME} completed <<<");

except Exception as e:
    logger.exception(e)
    raise e;

STAGE_NAME2 = "Data Validation Pipeline";

try:
    logger.info(f">>> stage {STAGE_NAME2} started <<<");
    obj = DataValidationPipeline();
    obj.initiate_data_validation();
    logger.info(f">>> stage {STAGE_NAME2} completed <<<");

except Exception as e:
    logger.exception(e);
    raise e;

STAGE_NAME3 = "Data Transformation Pipeline";

try:
    logger.info(f">>> stage {STAGE_NAME3} started <<<");
    obj = DataTransformationPipeline();
    obj.initiate_transformation();
    logger.info(f">>> stage {STAGE_NAME3} completed <<<");

except Exception as e:
    logger.exception(e);
    raise e;


