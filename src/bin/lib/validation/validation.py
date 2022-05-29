class Validator:
    """
    """
    def __init__(self, collectionDF):
        """
        CollectionDF (pd.DataFrame): output dataframe from Data 
            Collection Component.
        """
        self.collectionDF = collectionDF


class Schema(Validator):
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