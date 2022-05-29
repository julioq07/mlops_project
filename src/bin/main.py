from log.log import Logger

from lib.collection.collection import LocalCollector

from lib.validation.validation import Schema

from lib.preprocessing.preprocessing import Statistic, Transformer

from lib.training.training import LocalTrainer

from conf.modelA import conf as MConfA


DATASET_NAME = MConfA["collection.name"]
TRASH_FEATURES = MConfA["transform.trashFeatures"]
TARGET_FEATURE = MConfA["transform.targetFeature"]
TEST_SIZE = MConfA["train.test_size"]
RANDOM_STATE = MConfA["train.random_state"]


def main():
    print("=== Running ML Workflow ===")
    
    # # Set Logs Conf
    # Logger()

    # Data Collection Component
    print("=== Collection Started ===")
    colObjA = LocalCollector(DATASET_NAME)
    collectionDF = colObjA.load_csv()
    print("=== Collection Ended ===")

    # Data Validation Component
    print("=== Validation Started ===")
    print("=== --- Schema --- ===")
    schObjA = Schema(collectionDF)
    schObjA.get_schema()
    print("=== Validation Ended ===")

    # Data Preprocessing Component
    print("=== Preprocessing Started ===")
    print("=== --- Stats --- ===")    
    statObjA = Statistic(collectionDF)
    statObjA.get_describe()
    print("=== --- Transform --- ===")
    transObj = Transformer(collectionDF)
    transObj._set_input(TRASH_FEATURES)
    transObj._set_target(TARGET_FEATURE)
    print("=== Preprocessing Ended ===")

    # Data Training Component
    print("=== Training Started")
    trainer = LocalTrainer(
                    collectionDF=collectionDF,
                    trashFeatures=TRASH_FEATURES,
                    targetFeature=TARGET_FEATURE,
                    test_size=TEST_SIZE, 
                    random_state=RANDOM_STATE)
    trainer.train()
    logger = Logger(trainer.MODEL_NAME,
                    trainer.METRIC,
                    trainer.scores,
                    trainer.ARTIFACT)
    logger.write_log()
    print("=== Training Ended")

    # Data Deployment Component
    #
    
    print("=== ML Workflow Ended ===")


if __name__=="__main__":
    main()