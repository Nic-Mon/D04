#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body
def guess_num():
	tries = 0
	x = random.randint(1,25)
	while tries < 5:
		try:
			guess = int(input('Guess the number from 1 to 25: '))
			if(x == guess):
				print("Correct!")
				break
			elif(guess < 1 or guess > 25):
				print("Must be between 1 and 25")
			elif(guess < x):
				print("Too Low")
			elif(guess > x):
				print("Too High")
		except:
			print("Not an int!")
		tries += 1
	else:
		print("Too many tries, the number was " + str(x))



################################################################################
def main():


    guess_num()
    

if __name__ == '__main__':
    main()