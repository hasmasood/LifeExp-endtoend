# LifeExp-endtoend
This is end to end project on predicting life expectancy with data science approaches

## Technology stack
[Windows Subsytem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)

[Amazon Web Services (AWS)](https://aws.amazon.com/)

[Visual Studio Code](https://code.visualstudio.com/)

[Docker](https://www.docker.com/)

[HerokuAccount](http://heroku.com)

## Working environment
Create working environment aws_env using environment.yml file
```
conda env create -f environment.yml
```


## Deployment environment
We create a separate environment to deploy the code, working on Python 3.7.0.
```
conda create -n depl_env python==3.7.0
```
Install the required libraries (listed in requirements.txt) in the deployment environment.
```
conda activate depl_env
pip install -r requirements.txt
```
## Contents
[Step1-EDA.ipynb](https://github.com/hasmasood/LifeExp-endtoend/blob/main/Step1-EDA.ipynb)
A simple exploratory data analysis by sourcing raw data from one S3 bucket and exporting processed data to another bucket. An important tool facilitating the understanding, cleaning and wrangling of data is ```pandas_profiling```, and ``` featurewiz ``` is invaluable for feature selection.

[Step2-MLDev.ipynb](https://github.com/hasmasood/LifeExp-endtoend/blob/main/Step2-MLDev.ipynb)
This describes the process of feature engineering, machine learning model development, assessment and visualization of predictive performance. A number of models are evaluated and hyperparameters tuned via grid search pipelines. The best model selected is later trained from scratch. Models are exported using ```pickle```.

 [Step3-Deploy.ipynb](https://github.com/hasmasood/LifeExp-endtoend/blob/main/Step3-Deploy.ipynb)
 This deploys the model both locally as well as web service and make predictions for a sample data. 