# **`Wafer Fault Detection Project`**
## The aim of this project is to develop an automated sensor fault detection system for Scania trucks that can identify and diagnose sensor faults in real-time. The system should be able to detect faults in a wide range of sensors, including those used to monitor engine performance, fuel efficiency, and safety features. The goal is to improve the overall reliability and safety of Scania trucks by quickly identifying and addressing sensor faults, reducing the risk of accidents and downtime caused by equipment failure.

### Dataset is taken from Kaggle and stored in mongodb.

## Poblem Statement:  
### The inputs of various sensors for different wafers have been provided. In electronics, a wafer (also called a slice or substrate) is a thin slice of semiconductor used for the fabrication of integrated circuits. The goal is to build a machine learning model which predicts whether a wafer needs to be replaced or not(i.e., whether it is working or not) based on the inputs from various sensors. There are two classes: +1 and -1. 

- ## +1 means that the wafer is in a working condition and it doesn’t need to be replaced.

- ## -1 means that the wafer is faulty and it needs to be replaced. 

## Data Description - 
### The client will send data in multiple sets of files in batches at a given location. Data will contain Wafer names and 590 columns of different sensor values for each wafer. The last column will have the "Good/Bad" value for each wafer.

## "Good/Bad" column will have two unique values +1 and -1.  

 - ## "+1" represents Good wafer.

- ## "-1" represents Bad Wafer. 


* ## Applications Used
1. [Python 3.9](https://www.python.org/)
2. [Anaconda](https://www.anaconda.com/)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [ThunderClient](https://www.thunderclient.com/)
5. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
6. [Github Account](https://github.com)
7. [Docker](https://www.docker.com/)
8. [Render](https://render.com/)


* ## **How to setup ?**
1. ## Create a new environment
```
conda create --prefix env/<env_name> python=3.9 -y
```
2. ## Activate the newly created environment
```
conda activate env/<env_name>
```
3. ## Install the requirements
```
pip install -r requirements.txt
```

> ## Try it out at [Wafer Fault Detector]()