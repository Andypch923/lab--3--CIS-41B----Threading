from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from collections import namedtuple
#Scrape table off website, store in namedTuple and create a list of namedtuples storing data 
#of CO2 equivalent mixing ratio
class AGGIScraper:

    def __init__(self):
        #Using beautiful soup to scrape table of class wikitable sortable from website
        # to get table of data
        myUrl = "https://gml.noaa.gov/aggi/aggi.html"
        uClient = uReq(myUrl)
        page_lxml = uClient.read()
        page_soup = bs(page_lxml,"lxml")
        co2_dataNamedTuple = namedtuple('co2_dataNamedTuple',['year','co2','ch4','n2o','cfcs','hcfcs','hfcs','total','totalInPPM','AGGI','AGGIPercentage'])
        co2table = page_soup.find("table",{"class":"table table-bordered table-condensed table-striped table-header"})

        self.__listOfCO2EquivalentsData = []

        #store data of each row from table to namedTuple and append it to a list object listOfCO2Data
        count = 0

        for i in co2table.find_all('tr'):
            if count > 1:
                x = i.text.split('\n')
                x = list(filter(None,x))
                if count == 2:
                    x.append('')
                tempNamedTuple = co2_dataNamedTuple(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10])
                self.__listOfCO2EquivalentsData.append(tempNamedTuple)
            count += 1

    #return private list listOfCO2Data
    def getlistOfCO2EquivalentsData(self):
        return self.__listOfCO2EquivalentsData


    