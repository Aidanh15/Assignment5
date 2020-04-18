import requests 
import csv
import os
from bs4 import BeautifulSoup
import time

global last_called
#def parseData():
while True:

    url = "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=DCDRA&NumMins=90&format=xml"
    start_url = requests.get(url)
    
    soup = BeautifulSoup(start_url.text, "xml")
    data = []

    station = soup.find_all("Stationfullname") 
    origin = soup.find_all("Origin")
    departure = soup.find_all("Origintime")
    arrival = soup.find_all("Destinationtime")
    due = soup.find_all("Duein")
    late_arrival = soup.find_all("Late")
    global last_called
    last_called = soup.find("Querytime")
  

    for i in range(0, len(station)):
        data.append([station[i].text, origin[i].text, departure[i].text, arrival[i].text, due[i].text, late_arrival[i].text])
        
    #return f"""{data}"""
    print(data)


    
    # so ive tried two different approaches to saving the parsed data into a csv file

    #approach 1
    """with open('trainData.csv', 'w', newline="") as f:
        writer = csv.DictWriter(f,["station","origin","departure","arrival","due","late_arrival"])
        writer.writeheader()
        for text in data:
            writer.writerow(text)

    time.sleep(5 * 60)"""
  

  #approach 2
  # I think ths approach may work, its returning an error   'list' object has no attribute 'keys'

    # specifying the fields for csv file 
    fields = ['station', 'origin', 'departure', 'arrival', 'due', 'late_arrival'] 
  
    # writing to csv file 
    filename = "trains.csv"
    with open(filename, 'w') as csvfile: 
  
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
  
        # writing headers (field names) 
        writer.writeheader() 
  
        # writing data rows 
        writer.writerows(data)


        time.sleep(5 * 60)