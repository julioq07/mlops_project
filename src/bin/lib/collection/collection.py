
import os
import pandas as pd


class ExampleGen:
    """
    """

    def __init__(self, dataset_name):
        """
        """
        self.dataset_name = dataset_name


class LocalCollection(ExampleGen):
    """
    """
    DIR_PATH = os.getcwd()
    DATA_PATH = "../data"

    os.chdir(DATA_PATH)
    
    def __init__(self, dataset_name):
        super().__init__(dataset_name)
        self.file_name = f'{self.DATA_PATH}/{self.dataset_name}'
    
    def load_csv(self):
        file_path = f'{self.file_name}.csv'
        df = pd.read_csv(file_path)
        return df


class CloudCollection(ExampleGen):
    """
    """
    CLOUD_PATH = ''

    def __init__(self, dataset_name):
        super().__init__(dataset_name)

    def load(self):
        print("CloudCollection in construction")