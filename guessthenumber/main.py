import random
import sys

number = random.randint(1, 100)
guess = None
attempts = 0
n = (
    str(input("How many attempts would you like to have? Hard(H) or Easy(E): "))
    .strip()
    .upper()
)
if n == "H":
    attempts = 5
elif n == "E":
    attempts = 10
else:
    print("Please enter H or E.")
    sys.exit()

while guess != number and attempts > 0:
    guess = int(input("Guess the number (1-100): "))
    if guess < number:
        attempts -= 1
        print("Too low!")
        print("You have", attempts, "attempts left.")
    elif guess > number:
        attempts -= 1
        print("Too high!")
        print("You have", attempts, "attempts left.")

if guess == number:
    print("Congratulations! You guessed the number.")
else:
    print("Sorry, you ran out of attempts. The number was", number)
