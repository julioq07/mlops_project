from log.log import Logger

from lib.collection.collection import LocalCollector
from conf.modelA import modelA 

from lib.validation.validation import Schema

from lib.preprocessing.preprocessing import Statistic, Transformer


DATASET_NAME = modelA["collection.name"]


def main():
    print("=== Running ML Workflow ===")
    
    # Set Logs Conf
    Logger()

    # Data Collection Component
    print("=== Collection Started ===")
    colObjA = LocalCollector(DATASET_NAME)
    dfA = colObjA.load_csv()
    print("=== Collection Ended ===")

    # Data Validation Component
    print("=== Validation Started ===")
    print("=== --- Schema --- ===")
    schObjA = Schema(dfA)
    schObjA.get_schema()
    print("=== Validation Ended ===")

    # Data Preprocessing Component
    print("=== Preprocessing Started ===")
    print("=== --- Stats --- ===")    
    statObjA = Statistic(dfA)
    statObjA.get_describe()
    print("=== --- Transform --- ===")
    tranObjA = Transformer(dfA)
    dfTransA = tranObjA.identity()
    print("=== Preprocessing Ended ===")

    # Data Training Component
    print("=== Training Started")
    print("=== Training Ended")

    print("=== ML Workflow Ended ===")


if __name__=="__main__":
    main()