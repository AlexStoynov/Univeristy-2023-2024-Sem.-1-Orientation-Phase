playerCounter = 'A'

def marks(playerCounter):
    marks = []
    while True:

        inputMark = input("Input a mark for player " + str(playerCounter) + ": ")

        if inputMark == "":
            break
        elif inputMark == "x":
            mark = None
        else:
            mark = int(inputMark)

        marks.append(mark)
    return marks

marksA = marks(playerCounter)
playerCounter = 'B'
marksB = marks(playerCounter)

def findHighest(marks):
    if len(marks) == 0:
        highest = None
    else:
        highest = marksA[0]

        for index in range(1, len(marksA)):

            if marksA[index] == None:
                break 
            elif highest == None:
                highest = marksA[index] 
            elif marks[index] > highest:
                highest = marks[index]

    return highest

highestA = findHighest(marksA)
highestB = findHighest(marksB)

def decideWinner(highestA, highestB):
    if highestA == None:
        if highestB == None:
            winners = []
        else:
            winners = ["B"]
    else:
        if highestB == None:
            winners = ["A"]
        else:
            if highestA > highestB:
                winners = ["A"]
            elif highestA < highestB:
                winners = ["B"]
            else:
                winners = ["A", "B"]

    return winners

winners = decideWinner(highestA, highestB)

def printer(winners):
    if len(winners) == 0:
        print("Nobody wins.")
    elif len(winners) == 1:
        print("Player " + winners[0] + " wins.")
    else:
        print("It is a tie between player", winners[0], "and player", winners[1] + ".")
        
printer(winners)