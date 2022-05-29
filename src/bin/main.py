from log.log import Logger

from lib.collection.collection import LocalCollection
from conf.modelA import modelA 

from lib.validation.validation import Schema

from lib.preprocessing.preprocessing import Statistic, Transform


DATASET_NAME = modelA["collection.name"]


def main():
    print("=== Running ML Workflow ===")
    
    # Set Logs Conf
    Logger()

    # Data Collection Component
    print("=== Collection Started ===")
    colObj = LocalCollection(DATASET_NAME)
    df = colObj.load_csv()
    print("=== Collection Ended ===")

    # Data Validation Component
    print("=== Validation Started ===")
    print("=== --- Stats --- ===")    
    statObj = Statistic(df)
    statObj.get_describe()
    print("=== Validation Ended ===")

    # Data Preprocessing Component
    print("=== Preprocessing Started ===")
    print("=== --- Schema --- ===")
    schObj = Schema(df)
    schObj.get_schema()
    print("=== --- Transform --- ===")
    tranObj = Transform(df)
    tranObj.get_transform()
    print("=== Preprocessing Ended ===")

    print("=== ML Workflow Ended ===")


if __name__=="__main__":
    main()