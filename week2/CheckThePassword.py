password = input("Please define your password: ")

def passwordGuesser(password):
        
    tries = 2
    
    for x in range (0, 3):

        passwordTry = input("Please enter your password: ")

        if passwordTry != password:
            if tries == 0:
                print("Password incorrect")
                print("You have no more tries")  
                print("Your account has been blocked")
                break
            else:   
                print("Password incorrect")
                print("You have " + str(tries) + " more tries!")
        else:
            print("Password correct")
            break

        tries -= 1

passwordGuesser(password)