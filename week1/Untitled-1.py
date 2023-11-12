p1Name = input("Player one enter your name: ")
p2Name = input("Player two enter your name: ")
p1Score = input("Player one enter your score: ")
p2Score = input("Player two enter your name: ")

if p1Score > p2Score:
    print(str(p1Name) + " wins with " + str(p1Score) + " points!")
else:
    print(str(p2Name) + " wins with " + str(p2Score) + " points!")
