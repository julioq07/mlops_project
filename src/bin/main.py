import collections
from log.log import Logger

from lib.collection.collection import LocalCollection
from conf.collection import modelA  


DATASET_NAME = modelA["collection.name"]


def main():
    print("=== Running ML Workflow ===")
    
    Logger()

    # Data Collection Component
    print("=== Collection Started ===")
    colObj = LocalCollection(DATASET_NAME)
    df = colObj.load_csv()
    print(df.info)
    print("=== Collection Ended ===")

    print("=== ML Workflow Ended ===")

if __name__=="__main__":
    main()