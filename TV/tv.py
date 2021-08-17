# WAP to show whether watching TV is affected by the size of the screen

import numpy as np 
import csv
from plotly import plot
import plotly.express as px
import pandas as pd 

def plotFigure(data_path):
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        fig = px.scatter(csv_reader, x = "Size of TV", y = "\tAverage time spent watching TV in a week (hours)")
        fig.show()
        
def getDataSource(data_path):
    size_of_tv = []
    average_time_spent = []
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            average_time_spent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
        return {"x": size_of_tv, "y": average_time_spent}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("The correlation is ", correlation[0,1])

def setup():
    data_path = "tv sales/tv_sales.csv"
    data_source = getDataSource(data_path)
    plotFigure(data_path)
    findCorrelation(data_source)

setup() 

# We conclude the dataset is negative and low in correlation. Hence, People do not care about the size of the TV.
 