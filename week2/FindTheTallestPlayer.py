def inputPlayers():

    playerNames = []
    playerHeights = []
    playerNums = 1

    while True:

        inputName = input("Please enter player " + str(playerNums) + " 's name ")
        inputHeight = input("Please enter player " + str(playerNums) + " 's height ")

        if len(inputName) == 0:
            break

        playerNames.append(inputName)

        if len(inputHeight) < 0:
            print("Invalid Height")
            playerNames.remove(inputName)
            break

        playerHeights.append(inputHeight)
        playerNums += 1

    playerNamesAndHeights = []
    playerNamesAndHeights.append(playerNames)
    playerNamesAndHeights.append(playerHeights)

    return playerNamesAndHeights
    
playersInfo = inputPlayers()
playerNames = playersInfo[0]
playerHeights = playersInfo[1]

tallestPlayerHeight = max(playerHeights)
tallestPlayerIndex = playerHeights.index(tallestPlayerHeight)

print("The tallest player is " + str(playerNames[tallestPlayerIndex]) + " with height of " + str(tallestPlayerHeight))