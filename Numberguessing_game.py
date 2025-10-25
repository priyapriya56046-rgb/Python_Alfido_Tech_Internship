# Number Guessing Game
import random

number = random.randint(1, 100)
guess = 0
attempts = 0

print("Welcome! Guess the number between 1 and 100.")

while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    difference = abs(number - guess)
    if guess < number:
        print("Too low!", end=" ")
    elif guess > number:
        print("Too high!", end=" ")
    
    if difference <= 5 and guess != number:
        print("You're very close!")
    elif difference <= 10 and guess != number:
        print("Getting closer!")
    else:
        print()
        
print(f"Congrats! You guessed the number {number} in {attempts} attempts.")
