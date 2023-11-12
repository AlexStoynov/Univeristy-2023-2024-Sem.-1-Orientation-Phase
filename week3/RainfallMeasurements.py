rainfallNumbers = []

average = lambda numbers : float(sum(numbers)) / len(numbers)

def inputMeasurements():

    raindropsBelow2P5 = []
    raindropsAbove2P5 = []

    inputNum = input("Please enter a number: ")
    inputNums = []

    while True:

        if len(inputNum) == 0:
            break

        if float(inputNum) < 2.5:
            raindropsBelow2P5.append(float(inputNum))

        else:
            raindropsAbove2P5.append(float(inputNum))

        inputNums.append(float(inputNum))
        inputNum = input("Please enter a number: ")

    return inputNums

averageSegment = lambda numbers, start, end : average(numbers[start : end + 1])

def averageWeek(numbers):

    weeksAvgs = []

    if len(numbers) % 7 == 0:
        ranger = len(numbers) / 7

        for x in range(0, len(numbers), 7):
            weeksAvgs.append(averageSegment(numbers, x, 6 + x))
    else:
        ranger = len(numbers) / 7

        for x in range(int(ranger)):
            weeksAvgs.append(averageSegment(numbers, x * 7, 6 + x * 7))

        weeksAvgs.append(averageSegment(numbers, len(numbers) - len(numbers) % 7, len(numbers)))

    return weeksAvgs

def averageMonth(numbers):

    monthAvgs = []

    if len(numbers) % 30 == 0:
        for x in range(0, len(numbers), 30):
            monthAvgs.append(averageSegment(numbers, x, x + 29))
            
    else:
        ranger = len(numbers) / 30
        for x in range(int(ranger)):
            monthAvgs.append(averageSegment(numbers, x * 30, x * 30 + 29))
        monthAvgs.append(averageSegment(numbers, len(numbers) - len(numbers) % 30, len(numbers)))

    return monthAvgs

def printer():

    rainfallMeasurements = inputMeasurements()

    measurementsAverage = average(rainfallMeasurements)
    weeklyMeasurements = averageWeek(rainfallMeasurements)
    monthlyMeasurements = averageMonth(rainfallMeasurements)
    
    print("The average is: " + str(measurementsAverage) + " mm.")

    weekCounter = 1
    monthCounter = 1

    for measurementByWeek in weeklyMeasurements:
        print("Week " + str(weekCounter) + "'s average is: " + str(measurementByWeek) + " mm.")
        weekCounter += 1

    for measurementByMonth in monthlyMeasurements:
        print("Month " + str(monthCounter) + "'s average is: " + str(measurementByMonth) + " mm.")
        monthCounter += 1

printer()