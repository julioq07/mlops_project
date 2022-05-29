class Preprocessing:
    """
    """
    def __init__(self, collectionDF):
        """
        CollectionDF (pd.DataFrame): output dataframe from Data 
            Collection Component.
        """
        self.collectionDF = collectionDF


class Statistic(Preprocessing):
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


class Transform(Preprocessing):
    """
    """
    def __init__(self, collectionDF):
        super().__init__(collectionDF)

    def identity(self):
        """
        """
        df = self.collectionDF
        return df
    
    def get_otherTrans(self):
        pass
