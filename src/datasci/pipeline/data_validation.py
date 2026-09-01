from src.datasci.config.configuration import ConfigurationManager;
from src.datasci.components.data_validation import (DataValidation)
from src.datasci import logger

STAGE_NAME = "Validation Pipeline"

class DataValidationPipeline:
    def __init__(self):
        pass;

    def initiate_data_validation(self):
        config = ConfigurationManager();
        data_val_config = config.getDataValidationConfig();
        data_valid = DataValidation(data_val_config);
        data_valid.validate_all_columns();

if __name__ == '__main__':
    try:
        logger.info(f">>> stage {STAGE_NAME} started <<<");
        obj = DataValidationPipeline();
        obj.initiate_data_validation();
        logger.info(f">>> stage {STAGE_NAME} completed <<<");
    except Exception as e:
        logger.exception(e)
        raise e;