from lib.preprocessing.preprocessing import Transformer
from sklearn.model_selection import train_test_split
from model.modelA import ModelA


class Trainer(Transformer):
    """
    """
    def __init__(self, collectionDF):
        """
        """
        self.collectionDF = collectionDF
    
    def train(self):
        pass


class LocalTrainer(Trainer, Transformer, ModelA):
    """
    """
    def  __init__(self,
                  collectionDF,
                  trashFeatures,
                  targetFeature, 
                  test_size, 
                  random_state):
        self.collectionDF = collectionDF
        self.inputDF = self._set_input(trashFeatures)
        self.targetFeature = self._set_target(targetFeature)
        self.test_size = test_size
        self.random_state = random_state
        self.inputTrain = None
        self.inputTest = None
        self.targetTrain = None 
        self.targetTest = None
        self.scores = None

    def _set_split(self):
        """
        """
        print(self.inputDF)
        quit
        xtr, xte, ytr, yte = train_test_split(
                                        self.inputDF, 
                                        self.targetFeature, 
                                        test_size=self.test_size, 
                                        random_state=self.random_state)
        self.inputTrain = xtr
        self.inputTest = xte
        self.targetTrain = ytr 
        self.targetTest = yte

    def _get_model_output(self):
        X_train = self.inputTrain
        y_train = self.targetTrain 
        X_test = self.inputTest
        y_test = self.targetTest
        self.scores = self.model(X_train, y_train, X_test, y_test)
        return self.scores
    
    def train(self):
        self._set_split()
        self._get_model_output()
        

class CloudTrainer(Trainer):
    """
    """
    def __init__(self, collectionDF):
        super().__init__(collectionDF)
    
    def _set_trainer(self):
        """Point to cloud model code to train using collectionDF
        """
        print("CloudTrainer in construction")