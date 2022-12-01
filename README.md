# Welcome to RohanML Framework


***
## Summary

This project is a first approach for create a ML Workflow[2] in order to
apply basic concepts of MLOps paradigm to solve real production problems[4].

To reach my purpose, I developed an entire Framework (that I called RohanML), that
could be scaled without any problem for more than a couple models.

The next step could be use K8 in order to managing the executions of the models
tested but considering each MLPipeline component as an image and finally connected 
with an API Rest in order to offer to the client an MLaaS.


***
## Setup

Make sure your are located in the project root path:

    $ pwd
    ~/mlops_project


Then setup the conda environment:

    $ conda remove --name mlops --all
    $ conda env create -f env.yml
    $ conda activate mlops


Execute the shell script:

    $ sh ./src/opt/exe.sh


***
## References

1. Model: https://www.kaggle.com/code/jchen2186/machine-learning-with-iris-dataset/notebook

2. Dessing Pattern: “Machine Learning Design Patterns by Valliappa Lakshmanan, Sara
                     Robinson, and Michael Munn (O’Reilly). Copyright 2021 Valliappa
                     Lakshmanan, Sara Robinson, and Michael Munn, 978-1-098-11578-4.”

3. Anaconda Docu: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#removing-an-environment

3. MLFlow Logger: https://mlflow.org/docs/latest/quickstart.html

4. MLOps Big 8's: https://towardsdatascience.com/comparing-cloud-mlops-platform-from-a-former-aws-sagemaker-pm-115ced28239b


***
## Contact

Intellectual Author & Developer: Julio Quiñones