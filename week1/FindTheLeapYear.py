inputYear = input("Please enter a year: ")
if int(inputYear) % 400 == 0:
    if int(inputYear) % 100 == 0:
        print("The year you entered is a leap year")
elif int(inputYear) % 4 == 0:
    if int(inputYear) % 100 != 0:
        print("The year you entered is a leap year")
else:
    print("The year you entered is NOT a leap year!")