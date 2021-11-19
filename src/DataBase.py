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

    def fetchYears(self):
        conn = sqlite3.connect('GreenhouseGas.db')
        cursor = conn.cursor()
        cursor.execute('SELECT Year FROM GreenhouseGasTable') 
        items = [ x[0] for x in cursor.fetchall()]  
        return items

    def fetchCO2(self):
        conn = sqlite3.connect('GreenhouseGas.db')
        cursor = conn.cursor()
        cursor.execute('SELECT CO2 FROM GreenhouseGasTable')        
        items = [ x[0] for x in cursor.fetchall()]  
        return items

    def fetchCH4(self):
        conn = sqlite3.connect('GreenhouseGas.db')
        cursor = conn.cursor()
        cursor.execute('SELECT CH4 FROM GreenhouseGasTable')        
        items = [ x[0] for x in cursor.fetchall()]  
        return items
    
    def fetchN2O(self):
        conn = sqlite3.connect('GreenhouseGas.db')
        cursor = conn.cursor()
        cursor.execute('SELECT N2O FROM GreenhouseGasTable')        
        items = [ x[0] for x in cursor.fetchall()]  
        return items

    def fetchCFCs(self):
        conn = sqlite3.connect('GreenhouseGas.db')
        cursor = conn.cursor()
        cursor.execute('SELECT CFCs FROM GreenhouseGasTable')        
        items = [ x[0] for x in cursor.fetchall()]  
        return items
    
    def fetchHCFCs(self):
        conn = sqlite3.connect('GreenhouseGas.db')
        cursor = conn.cursor()
        cursor.execute('SELECT HCFCs FROM GreenhouseGasTable')        
        items = [ x[0] for x in cursor.fetchall()]  
        return items
    
    def fetchHFCs(self):
        conn = sqlite3.connect('GreenhouseGas.db')
        cursor = conn.cursor()
        cursor.execute('SELECT HFCs FROM GreenhouseGasTable')        
        items = [ x[0] for x in cursor.fetchall()]  
        return items