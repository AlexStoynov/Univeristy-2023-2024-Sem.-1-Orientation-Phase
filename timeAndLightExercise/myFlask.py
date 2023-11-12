from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)
timeLightList = []

def getCurrentTime():
    rightNow = datetime.now()
    formattedTime = rightNow.strftime("%I:%M%p").lstrip('0').lower()
    day = rightNow.strftime("%A")
    return f"It is {formattedTime} on {day}."

def generatePairs():
    timeLightTuple = (getCurrentTime(), random.randint(0, 1000))
    if len(timeLightList) >= 25:
        timeLightList.pop(0)
        timeLightList.append(timeLightTuple)
    else:
        timeLightList.append(timeLightTuple)
    return timeLightList

@app.route('/')
def displayData():
    timeLightPairs = generatePairs()
    
    return render_template('index.html', timeLightPairs=timeLightPairs)

if __name__ == '__main__':
    app.run(debug=True)
