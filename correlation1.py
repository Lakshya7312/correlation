import pandas as pd
import plotly_express as px
import numpy as np
import csv

def getDataSource(dataPath):
    marksInPercentage = []
    daysPresent = []

    with open(dataPath) as csv_file:
        f = csv.DictReader(csv_file)
        for i in f:
            marksInPercentage.append(float(i["Marks In Percentage"]))
            daysPresent.append(float(i["Days Present"]))

    return {"x": daysPresent, "y": marksInPercentage}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(correlation)

def setup():
    dataPath = "C:/Users/Accounts/Desktop/Python Projects/cor1.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()

data = pd.read_csv("C:/Users/Accounts/Desktop/Python Projects/cor1.csv")

graph = px.scatter(data, x="Marks In Percentage", y="Days Present")
graph.show()