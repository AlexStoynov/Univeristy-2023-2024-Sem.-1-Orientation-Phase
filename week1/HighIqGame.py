while(True):
    num = input("Please enter a number lower than 10- ")
    sum = int(num) + 1
    if sum < 10:
        print(sum)
        print("I win!")
    else:
        print("The number you entered is equal or higher than 9!")

    print("Do you want to play again?")
    playerInput = input("Yes or No- ")

    if playerInput == "Yes":
        continue
    elif playerInput == "No":
        print("Thanks for playing!")
        break