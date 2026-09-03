import pandas as pd;
import os
from src.datasci import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.datasci.config.configuration import ConfigurationManager;
from src.datasci.components.model_selection import (ModelTrainer)

STAGE_NAME = "Model Training";

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_train(self):
        config = ConfigurationManager();
        model_trainer_config = config.get_model_trainer_config();
        model_trainer_config = ModelTrainer(config=model_trainer_config);
        model_trainer_config.train();

if __name__ == '__main__':
    try:
        logger.info(f">>> stage {STAGE_NAME} started <<<");
        obj = ModelTrainingPipeline();
        obj.initiate_model_train();
        logger.info(f">>> stage {STAGE_NAME} completed <<<");
    except Exception as e:
        logger.exception(e)
        raise e;
