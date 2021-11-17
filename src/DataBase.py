import sqlite3
class DataBase:
    def __init__(self):
         #connect to a database
        conn = sqlite3.connect('GreenhouseGas.db')
        #create a cursor
        cursor =  conn.cursor()
        conn.close()

    def createTable(self,tempObj):
    #connect to a database
        conn = sqlite3.connect('GreenhouseGas.db')
    #create a cursor
        cursor =  conn.cursor()
    #create a Table
        cursor.execute("""CREATE TABLE GreenhouseGasTable(
                Year PRIMARY KEY,
                CO2 FLOAT,
                CH4 FLOAT,
                N2O FLOAT,
                CFCs FLOAT,
                HCFCs FLOAT,
                HFCs FLOAT,
                Total FLOAT,
                TotalinPPM INT,
                AGGI FLOAT,
                AGGIPercentageChange FLOAT
            )""")
        file_object = open("table.txt",'a')
        file_object.write("TableCreated")
        file_object.close()
    #parse list of namedTuples into table
        cursor.executemany("INSERT INTO GreenhouseGasTable VALUES(?,?,?,?,?,?,?,?,?,?,?)",tempObj)
    #commits commands
        conn.commit()
    #close our connection
        conn.close()

    #fetch country names for the top 10 countries with highest co2 emissions in 2017
    def fetch2017top10Countries(self):
        conn = sqlite3.connect('GreenhouseGas.db')
        cursor = conn.cursor()
        cursor.execute('SELECT Country FROM temperatureTable ORDER BY Fossil2017inPercentage DESC LIMIT 10')
        items = [ x[0] for x in cursor.fetchall()]  
        return items

    #fetch country emission percentages for the top 10 countries with highest co2 emissions in 2017
    def fetch2017top10Percentage(self):
        conn = sqlite3.connect('GreenhouseGas.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Fossil2017inPercentage FROM temperatureTable ORDER BY Fossil2017inPercentage DESC LIMIT 10")
        items = [ x[0] for x in cursor.fetchall()]  
        return items