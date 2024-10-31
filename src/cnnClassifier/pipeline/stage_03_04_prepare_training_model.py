from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.prepare_callbacks import PrepareCallbacks
from src.cnnClassifier.components.prepare_training_model import Training
from src.cnnClassifier import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainigPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallbacks(config = prepare_callbacks_config)
        #callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config = training_config)
        training.get_base_model()
        training.train_valid_generator()
        # training.train(
        #     callback_list = callback_list
        # )


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = ModelTrainigPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>> {STAGE_NAME} end <<<<<<<<<<<<<")
    except Exception as e:
        raise e
    