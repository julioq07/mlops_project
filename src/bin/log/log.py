import os
from mlflow import log_metric, log_param, log_artifacts


class Logger:
    """Class Logger

    Implement a Logger instance from MLFlow logs.
    """
    def __init__(self):
        """Class constructor
        
        Log for parameters, metrics, artifacts.
        """
        # Log a parameter (key-value pair)
        log_param("param1", 2021)

        # Log a metric; metrics can be updated throughout the run
        log_metric("metric1", 1)
        log_metric("metric2", 2)
        log_metric("metric1", 10)

        # Log an artifact (output file)
        if not os.path.exists("../logs"):
            os.makedirs("../logs")
        with open("../logs/log.txt", "w") as f:
            f.write("MLFlow Log Implementation")
        log_artifacts("../logs")

        print("=== Log Performed ===")
    