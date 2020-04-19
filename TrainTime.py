import requests
import csv
import os
from bs4 import BeautifulSoup
import time
from prettytable import PrettyTable 

#global last_called
def parseData():
    while True:

        url = "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CNLLY&NumMins=90&format=xml"
        start_url = requests.get(url)

        soup = BeautifulSoup(start_url.text, "xml")
        data = []

        station = soup.find_all("Stationfullname")
        origin = soup.find_all("Origin")
        departure = soup.find_all("Origintime")
        arrival = soup.find_all("Destinationtime")
        due = soup.find_all("Duein")
        late = soup.find_all("Late")
        #global last_called
        #last_called = soup.find("Querytime")

        for i in range(0, len(station)):
            data.append(
                [station[i].text, origin[i].text, departure[i].text, arrival[i].text, due[i].text+" min", late[i].text+" min"])

        # return f"""{data}"""
        print(data)



        
        # specifying the fields for csv file
        fields = ['station', 'origin', 'departure', 'arrival', 'due', 'late']

        # writing to csv file
        filename = "trains.csv"
        with open(filename, 'w') as file:

            writer = csv.writer(file, delimiter=',')
            writer.writerow(i for i in fields)
            for j in data:
                writer.writerow(j)


            # wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            # wr.writerow(data)

        return(False)
        #time.sleep(30)
        #return(True)
parseData()
