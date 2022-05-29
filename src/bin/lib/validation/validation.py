import collections


class ValidationGen:
    """
    """
    def __init__(self, collectionDF):
        """
        CollectionDF (pd.DataFrame): output dataframe from Data 
            Collection Component.
        """
        self.collectionDF = collectionDF


class StatisticGen(ValidationGen):
    """
    """
    def __init__(self, collectionDF):
        super().__init__(collectionDF)

    def get_describe(self):
        """
        """
        return self.collectionDF.describe()

    def get_otherStats(self):
        pass


class SchemaGen(ValidationGen):
    """
    """
    def __init__(self, collectionDF):
        super().__init__(collectionDF)
    
    def get_schema(self):
        """
        """
        return self.collectionDF.info()
    
    def get_otherSchemas(self):
        pass