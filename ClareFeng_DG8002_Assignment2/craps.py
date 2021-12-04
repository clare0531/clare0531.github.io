from random import randint


rollval=input("Welcome to Craps! Type ROLL to begin: ")
counter=0
while rollval.lower()!="quit":
	if rollval.lower()!="roll":
		rollval=input("Your Input doesn't make sense, Type ROLL to play, QUIT to exit: ")
	else:	
		dice1=randint(1,6)
		dice2=randint(1,6)
		score=dice1+dice2
		counter=counter+1
		print ("Dice 1:" + str(dice1))
		print ("Dice 2:" + str(dice2))
		print ("Total:" + str(score))
		
		if score==7 or score==11:
			print("You win!")
			break
		elif score==2 or score==3 or score==12:
			print("CRAPS! You lose! Better luck next time!")
			break
		else:
			rollval=input("You get to play another round! Type ROLL to play again, QUIT to exit: ")
		

print("Total number of rounds played:"+ str(counter))