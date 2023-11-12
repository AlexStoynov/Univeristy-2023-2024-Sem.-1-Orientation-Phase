import random

listOfWords = ["apple", "pear", "watermelon", "grapes", "kiwi", "pineapple", "dragon fruit", "peach", "orange"]

randomWordIndex = random.randint(0, len(listOfWords))
print(str(listOfWords[randomWordIndex]))