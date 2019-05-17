#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 9

import random

def secretNum():
    return random.randrange(1,21)
def userGuess():
    guess = int(input("Enter your guess from 1-20 "))
    return guess
def judgement(secret_num,guess):
    if (secret_num == guess):
        return print("Your guess was correct! ")
    elif (secret_num < guess):
        return print("Sorry. Your guess was too high. ")
    elif (secret_num > guess):
        return print("Sorry. Your guess was too low. ")

def main():
	repeat = ''
	while repeat != 'n':
		guess = 0
		secret_num = secretNum()
		while guess != secret_num:
			guess = userGuess()
			judgement(secret_num,guess)
		repeat = input("Would you like to try again? (y/n): ")
main()
