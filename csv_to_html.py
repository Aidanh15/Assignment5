
from prettytable import PrettyTable 
  
def createPage():  
    # open csv file 
    csvfile = open("trains.csv", 'r') 
    
    # read the csv file 
    csvfile = csvfile.readlines() 
    
    # Seperating the Headers 
    l1 = csvfile[0] 
    l1 = l1.split(',') 
    
    start = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="style.css"><meta http-equiv="refresh" content="33" >
    <link rel="icon" href="image/png" href="https://www.irishrail.ie/favicon.ico"/>
    <script src="script.js"></script>
    <title>Document</title>
</head>
<body> 
<h1>Real-Time Info</h1> 
<div class="tbl-content">"""


    end = """
</body>
</html>"""

    # headers for table 
    t = PrettyTable([l1[0], l1[1], l1[2], l1[3], l1[4], l1[5]]) 
    
    # Adding the data 
    for i in range(1, len(csvfile)) : 
        t.add_row(csvfile[i].split(',')) 
    
    
    code = t.get_html_string() 
    html_file = open('TrainTable.html', 'w') 
    html_file = html_file.write(start), html_file.write(code), html_file.write(end)

createPage()