import numpy as np
import csv;
import plotly.express as px

def getDataSource(data_path):
    marks =[]
    days_present =[]

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x" : marks, "y":days_present}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("correlation table: ", correlation)
    print("correlation : ", correlation[0,1])

def plotGraph(data_path):    
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Marks In Percentage", y="Days Present")
        fig.show()



def setup():
    data_path = "./Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotGraph(data_path)

setup()
