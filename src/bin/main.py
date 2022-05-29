from log.log import Logger

from lib.collection.collection import LocalCollection
from conf.modelA import modelA 

from lib.validation.validation import StatisticGen, SchemaGen


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
    statObj = StatisticGen(df)
    statObj.get_describe()

    print("=== --- Schema --- ===")
    schObj = SchemaGen(df)
    schObj.get_schema()
    print("=== Validation Ended ===")

    print("=== ML Workflow Ended ===")


if __name__=="__main__":
    main()