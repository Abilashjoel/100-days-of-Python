print()
print("Welconme to the Treasure Island")
print("Your mission is to find the treasure.")
print("You are in front of a road. Where do you want to go? Type 'left' or 'right'\n")
choice1 = input("Enter Your choice ").lower()
if choice1 == 'right':
    print("Game over. People of the jungle has seen you.")
else:
    choice2=input("You are in front of a river. What do you want to do? 'swim' or 'wait'\n").lower()
    if choice2 == 'swim':
         print("Game over. There were some crocodile into the river.")
    else:
        choice3 = input("You arrived at the island. There are 3 door inside a house. Go there and choose the door you want to enter with. Which door do you want to go? 'red', 'yellow', 'blue'?\n")
        if choice3 == 'red' or choice3 == 'blue':
            print("Game Over. You enter into the ghost room.")
        else: print("Congratulations!! You win.")
        
