import random

print (" welcome to stone,paper, Scissors python game")

option = int(input("0 for game start and 1 for game quite")) # Taking a input from a user to sarting a game 
if(option==0):
    print("game start......! ")
    print ("0 for stone, 1 for paper, 2 for scissors\n")

    element = ["stone" , "paper" , "scissors"]  # Creating a variable to store game data i.e. stone paper scissors 
    
    while (True):
        user_choice= int(input ("choose your option ")) #Take input from user

        if(user_choice>2 or user_choice<0):
            print(" invalid option!! \n choose number between 0 to 2 \n")

        else:    
            print (" you choose ",element [user_choice])
    
            computer_choice = random.randint(0, 2) # Taking a random value 
            print (" computer choose ",element[computer_choice])

            # for chacking winner 
            if(user_choice==computer_choice):
                print ("!!...... Match Draw.......!!\n ")
            elif((user_choice==0 and computer_choice==2) or (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==1)):
                print (" congratulations..... You Win...! \n ")

            else:
                print(" Oo No Computer Win......!\n")

else:
    print (" You exit a game  \n")