import pandas as pd


class Collector:
    """
    """

    def __init__(self, dataset_name):
        """
        """
        self.dataset_name = dataset_name


class LocalCollector(Collector):
    """
    """
    DATA_PATH = "./src/data"
    
    def __init__(self, dataset_name):
        super().__init__(dataset_name)
        self.file_name = f'{self.DATA_PATH}/{self.dataset_name}'
    
    def load_csv(self):
        file_path = f'{self.file_name}.csv'
        df = pd.read_csv(file_path)
        return df
    
    def load_other_types(self):
        # TODO document why this method is empty
        pass


class CloudCollector(Collector):
    """
    """
    CLOUD_PATH = ''

    def __init__(self, dataset_name):
        super().__init__(dataset_name)

    def load(self):
        print("CloudCollection in construction")