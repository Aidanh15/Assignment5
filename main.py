import TrainTime
import csv_to_html 
import time
import webbrowser
import sched
import time

initiate = TrainTime.parseData()
step2 = csv_to_html.createPage()
webbrowser.open_new_tab('file:///home/aidan/Desktop/vsCode%20projects/CS402/'+'TrainTable.html')

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print("Doing stuff...")
    initiate = TrainTime.parseData()
    step2 = csv_to_html.createPage()
    #webbrowser.open('file:///home/aidan/Desktop/vsCode%20projects/CS402/'+'TrainTable.html',0)

    s.enter(30, 1, do_something, (sc,))

s.enter(30, 1, do_something, (s,))
s.run()


"""def OpenPage():
    while True:
        initiate = TrainTime.parseData()

        step2 = csv_to_html.createPage()

        webbrowser.open_new_tab('file:///home/aidan/Desktop/vsCode%20projects/CS402/'+'TrainTable.html')

        
        time.sleep(40)
        return(False)
        return(True)"""

