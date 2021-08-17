# WAP to find out the correlation between temperature and ice cream sales

import plotly.express as px
import csv
import numpy as np 

def plotFigure(data_path): 
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales( ₹ )")
        fig.show()
        
def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            ice_cream_sales.append(float(row["Temperature"]))
            cold_drink_sales.append(float(row["Ice-cream Sales( ₹ )"]))
        return {"x": ice_cream_sales, "y": cold_drink_sales}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between Temperature vs Ice cream sales is ", correlation[0,1])
        
def setup():
    data_path = "Ice cream/Ice_cream_data.csv"
    data_source = getDataSource(data_path)
#findCorrelation(data_source)
    plotFigure(data_path)

setup()
    
# We conclude that the temperature does affect the ice creams sales because the correlation between them is positively high. 