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