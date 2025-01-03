import random

# generate a number, 1-10
secret_number = random.randint(1, 10)
guess = None

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else:
        print("You are a Winner!")