import matplotlib.pyplot as plt
import numpy as np
import WebScrapper
import DataBase
import threading

class GraphWrappers:
    def __init__(self):
        self.__AGGIScraperObj = WebScrapper.AGGIScraper()
        self.__DataBaseObj = DataBase.DataBase()
        
        self.__DataBaseObj.createTable()

class Graph:

    def linearRegression(self,x,y):
        x = np.array(x)
        y = np.array(y)
        plt.plot(x, y, 'o')
        m, b = np.polyfit(x, y, 1)
        plt.plot(x, m*x + b)
        plt.show()
