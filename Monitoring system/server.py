from flask import Flask
from flask import render_template
from flask import request, redirect
import random
from datetime import datetime
import csv 
import requests

list1 = []
list2 = []
average = 0
avgLightList = []
avgTempList = []
avgHumidityList = []
avgLightList1 = []
avgTempList1 = []
avgHumidityList1 = []
avgLightList2 = []
avgTempList2 = []
avgHumidityList2 = []

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
            

def average1(average_list):
    return sum(average_list) / len(average_list)


app = Flask(__name__)

@app.route('/')
def displayData():
    
    if list2 == []:
         return render_template('index.html', pairs= [])
    else:
        return render_template('index.html', time = list2[-1][0], temperature = list2[-1][1], humidity = list2[-1][2], light = list2[-1][3], id = list2[-1][4], average = average1(avgLightList), max = max(avgLightList), min = min(avgLightList))

@app.route('/post', methods = ['POST'])
def post():
    data = request.get_json()
    time = data['time']
    temperature = int(data['temperature'])
    humidity = int(data['humidity'])
    light = int(data['light'])
    id1 = data['id1']
    avgLightList.append(light)
    avgHumidityList.append(humidity)
    avgTempList.append(temperature)
    list1 = (time, temperature, humidity, light, id1)
    match list1[-1]:
        case 1:
            avgLightList1.append(light)
            avgHumidityList1.append(humidity)
            avgTempList1.append(temperature)
        case 2:
            avgLightList2.append(light)
            avgHumidityList2.append(humidity)
            avgTempList2.append(temperature)
        case 3:
            avgLightList1.append(light)
            avgHumidityList1.append(humidity)
            avgTempList1.append(temperature)

    if len(list2) >= 25:
        list2.pop(0)
        list2.append(list1)
    else:
        list2.append(list1)

    return "OK"