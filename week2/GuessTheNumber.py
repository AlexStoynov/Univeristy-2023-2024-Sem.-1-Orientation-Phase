import random
listOfScores = []

while True:

    randomNum = random.randint(1, 100)
    guess = input("Please try to guess the number: ")
    guesses = 1

    while guess != randomNum:

        if int(guess) > randomNum:
            print("Too high")
        elif int(guess) < randomNum:
            print("Too low")
        else:
            break

        guesses += 1
        guess = input("Please try to guess the number: ")

    print("Congratulations! You were able to guess the number in " + str(guesses) + " guesses.")
    listOfScores.append(guesses)
    yesOrNo = input("Do you want to play again? ")

    if yesOrNo == "Yes":
        continue
    elif yesOrNo == "No":
        break
    else:
        print("Invalid Answer!")

sumOfScores = sum(listOfScores)
avgOfScores = sumOfScores / len(listOfScores)
print("Thanks for playing! Your score average was: " + str("%.0f" % avgOfScores) + " and your best score was: " + str(min(listOfScores)))