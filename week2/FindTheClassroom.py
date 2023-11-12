studentName = input("Please enter your name: ")
studentSubject = input("Which subject are you studying? ")

classesAndRooms = {"Maths": 401, "English": 402 , "Biology": 403, "Computing": 404, "Electronics": 405}

classesAndRooms_keys = classesAndRooms.keys()

if studentSubject in classesAndRooms_keys:
    print("Hi " + str(studentName) + ", go to room " + str(classesAndRooms[studentSubject]) + " for " + str(studentSubject))
else:
    print("I don't know which room that class is in")
    exit