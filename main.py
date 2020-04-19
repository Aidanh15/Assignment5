import TrainTime
import csv_to_html 
import codecs
import time
import webbrowser


initiate = TrainTime.parseData()

step2 = csv_to_html.createPage()

webbrowser.open_new_tab('file:///home/aidan/Desktop/vsCode%20projects/CS402/'+'TrainTable.html')
#codecs.open("TrainTable.html", "r", "utf_8")