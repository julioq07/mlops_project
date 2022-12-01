from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from conf.modelA import conf as MConfA


class Modeler:
    """
    """
    MODEL_NAME = 'model_name'

    def __init__(self, inputTrain, targetFeature):
        """
        """
        self.inputTrain = inputTrain
        self.targetFeature = targetFeature
    
    def model(self):
        """
        """
        pass


class ModelA(Modeler):
    """
    """
    MODEL_NAME = 'Kmeans'
    METRIC = '1'
    ARTIFACT = '1'

    KRANGE = MConfA["train.krange"]

    def __init__(self, inputTrain, targetFeature):
        super().__init__(inputTrain, targetFeature)
    
    def model(self, X_train, y_train, X_test, y_test):
        """Model instance

        Returns: scores (dict): {n_neighbors: accuracy_score}
        """
        scores = {}
        for k in self.KRANGE:
            model = KNeighborsClassifier(n_neighbors=k)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            scores[k] = metrics.accuracy_score(y_test, y_pred)
        return scores