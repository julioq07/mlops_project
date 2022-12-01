import os
from mlflow import log_metric, log_param, log_artifacts


class Logger:
    """Class Logger

    Implement a Logger instance from MLFlow logs.
    """
    def __init__(self, model_name, metric, param, artifact):
        """Class constructor
        
        Log for parameters, metrics, artifacts.
        """
        self.model_name = model_name
        self.metric = metric 
        self.param = param 
        self.artifact = artifact
        # Log an artifact (output file)
        if not os.path.exists("../logs"):
            os.makedirs("../logs")
        with open("../logs/log.txt", "w") as f:
            f.write("MLFlow Log Implementation")
        print("=== Log Init ===")

    def _metric(self):
        """
        """
        log_metric(self.model_name, self.metric)
    
    def _param(self):
        """
        """
        log_param(self.model_name, self.param)

    def _artifacts(self):
        """
        """
        log_artifacts(self.model_name, self.artifact)

    def write_log(self):
        """
        """
        self._metric()
        self._param()
        # self._artifacts()
        print("=== Log written ===")