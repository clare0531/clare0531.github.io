import random

total = 0
i = 0

game = input("Welcome to Craps! Type ROLL to begin or QUIT to exit: ")
while total != 7 or total != 11 or total != 2 or total != 3 or total != 12:
    if game == 'ROLL' or game == 'roll' or game =='Roll': 
        i=i+1
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        total=dice1+dice2
        print ("Dice 1:", dice1)
        print ("Dice 2:", dice2)
        print ("Your total is:", total)
        if total == 7 or total == 11:
            print ("Congrats you won!\n")
            print ("Total number of rounds played: ", i)
            break
        elif total == 3 or total ==2 or total ==12:
            print ("Craps! You lost! \n")
            print ("Total number of rounds played: ", i)
            break
        else:
            game = input ("You get to play another round! \nType ROLL to play again or QUIT to exit:")
    elif game == 'QUIT' or game == 'Quit' or game == 'quit':
        quit()
    else:
        game = input("Invalid input, please try again: ")