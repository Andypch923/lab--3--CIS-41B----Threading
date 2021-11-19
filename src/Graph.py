import matplotlib.pyplot as plt
import numpy as np
import WebScrapper
import DataBase
import threading
import multiprocessing

class Graph:
    def __init__(self):
        self.__CO2Data = []
        self.__CH4Data = []
        self.__N2OData = []
        self.__CFCsData = []
        self.__HCFCsData = []
        self.__HFCsData = []

        self.__AGGIScraperObj = WebScrapper.AGGIScraper()
        self.__DataBaseObj = DataBase.DataBase()
        f = open("table.txt","a+")
        f.seek(0)
        if (f.read() == ""):
            f.close()
            self.__DataBaseObj.createTable(self.__AGGIScraperObj.getlistOfCO2EquivalentsData())

        self.__YearData = self.__DataBaseObj.fetchYears()

    def CO2Grapher(self):
        self.__CO2Data = self.__DataBaseObj.fetchCO2()
        linearRegression(self.__CO2Data,self.__YearData)

    def CH4Grapher(self):
        self.__CH4Data = self.__DataBaseObj.fetchCH4()
        linearRegression(self.__CH4Data,self.__YearData)

    def N2OGrapher(self):
        self.__N2OData = self.__DataBaseObj.fetchN2O()
        linearRegression(self.__N2OData,self.__YearData)
    
    def CFCsGrapher(self):
        self.__CFCsData = self.__DataBaseObj.fetchCFCs()
        linearRegression(self.__CFCsData,self.__YearData)
    
    def HCFCsGrapher(self):
        self.__HCFCsData = self.__DataBaseObj.fetchHCFCs()
        linearRegression(self.__HCFCsData,self.__YearData)

    def HFCsGrapher(self):
        self.__HFCsData = self.__DataBaseObj.fetchHFCs()
        linearRegression(self.__HFCsData,self.__YearData)

def linearRegression(x,y):
        tempList = list()
        for i in x:
            tempList.append(float(i))
        tempList2 = list()
        for i in y:
            tempList2.append(float(i))
        x = tempList
        y = tempList2
        x = np.array(x)
        y = np.array(y)

        fig, ax = plt.subplots()
        ax.plot(x, y, 'o')
        m, b = np.polyfit(x, y, 1)
        ax.plot(x, m*x + b)
        

def main():
    graphObj = Graph()
    t1 = threading.Thread(target = graphObj.CO2Grapher)
    t2 = threading.Thread(target = graphObj.CH4Grapher)
    t3 = threading.Thread(target = graphObj.N2OGrapher)
    t4 = threading.Thread(target = graphObj.CFCsGrapher)
    t5 = threading.Thread(target = graphObj.HCFCsGrapher)
    t6 = threading.Thread(target = graphObj.HFCsGrapher)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    plt.show()
main()