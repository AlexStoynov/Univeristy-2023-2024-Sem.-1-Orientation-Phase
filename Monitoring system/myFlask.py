import requests
import random
from datetime import datetime
import csv 
import pandas as pd
import json

list1 = []
list2 = []

def getCurrentTime():
    rightNow = datetime.now()
    formattedTime = rightNow.strftime("%I:%M%p").lstrip('0').lower()
    day = rightNow.strftime("%A")
    return f"It is {formattedTime} on {day}."

def generatePairs():
    tuple1 = (getCurrentTime(), random.randint(0, 1000))
    if len(list1) >= 25:
        list1.pop(0)
        list1.append(tuple1)
    else:
        list1.append(tuple1)
    return list1

def writeCSV(list2):
    if list2 != None:
        with open('values.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerows(list2)

while True:
    x = input("Generate new? yes/no: ")

    if x == "no":
        break

    time = getCurrentTime()
    humidity = random.randint(0, 100)
    light = random.randint(0, 1000)
    tempreture =random.randint(15, 40)
    id1 =random.randint(1, 10)
    list1 = []
    list1.append(time)
    list1.append(tempreture)
    list1.append(humidity)
    list1.append(light)
    list1.append(id1)

    list2.append(list1)
    print(list2[-1])
    data = { 'time': list2[-1][0], 'tempereture':list2[-1][1],'humidity':list2[-1][2], 'light': list2[-1][3],'id1':list2[-1][4] }
    with open("values.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['time'], row['temperature'], row['humidity'],  row['light'], row['id1'] )
            data = { 'time': row['time'], 'tempereture':row['temperature'],'humidity':row['humidity'], 'light': row['light'],'id1':row['id1'] }
            response = requests.post('http://127.0.0.1:5000/post', json = data)

    print(data)