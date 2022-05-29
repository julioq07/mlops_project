class Preprocessor:
    """
    """
    def __init__(self, collectionDF):
        """
        CollectionDF (pd.DataFrame): output dataframe from Data 
            Collection Component.
        """
        self.collectionDF = collectionDF


class Statistic(Preprocessor):
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


class Transformer(Preprocessor):
    """
    """
    def __init__(self, collectionDF):
        super().__init__(collectionDF)
        self.inputDF = None
        self.targetFeature = None

    def identity(self):
        """
        """
        return self.collectionDF
    
    def _set_input(self, trashFeatures):
        """Method to prepare the input dataframe.

        Args:
            trashFeatures (list): features non needed as input.
        
        Returns:
            X (pd.DataFrame)
        """
        df = self.collectionDF.drop(trashFeatures, axis=1)
        return df
    
    def _set_target(self, targetFeature):
        """Method to prepare the target feature.

        Args:
            targetFeature (str): feature to be predicted.
        
        Returns:
            y (pd.Series)
        """
        serie = self.collectionDF[targetFeature]
        return serie

    def _get_otherTrans(self):
        pass
