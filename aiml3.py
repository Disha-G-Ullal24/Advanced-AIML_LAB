import random

# Secret number between 1 and 50
secret = random.randint(1, 50)
attempts = 0
print("Guess the number between 1 and 50!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! The secret number was {secret}. Attempts: {attempts}")
        break
