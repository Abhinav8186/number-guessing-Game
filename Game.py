import random
print("Number Guessing Game")
name = input("Enter your name:- ")
number = random.randint(1,9)
chances = 0
print("Hi! ",name," Guess a number between 1 to 9: ")
print("You Have 5 chances to go!")

while chances < 5:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! YOU WON!")
        break

    elif guess < number:
        print("Guess is too low! Guess a number higher than",guess)
        
    else:
        print("Guess is too high! Guess a number lesser than",guess)
       
    chances += 1

    
if not chances < 5:
    print("You loose! Better Luck Next Time!")
    print("Well the number is: ",number)
