import random

print("Welcome to the number guessing game!")
print("/n Choose difficulty level")
print("1. Easy (1-10)")
print("2. Medium (1-20)")
print("3. Hard (1-50)")
print("4. Custom range")

def safe_int_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("You can only enter numbers.")

choice = safe_int_input("Enter your coice: ")

if choice == 1:
    low, high = 1, 10
    max_attempts = 5

elif choice == 2:
    low, high = 1, 20
    max_attempts = 7

elif choice == 3:
    low, high = 1, 50
    max_attempts = 10

elif choice == 4:
    low = safe_int_input("Enter the lowest or minimum number you want: ")
    high = safe_int_input("Enter the highest number that you want: ")
    max_attempt = int((high - low)/5) + 5

else:
    print("You entered an invalid choice, choosing medium by default.")
    low, high = 1, 20
    max_attempt = 10

secret_number = random.randint(low, high)
attempts = 0

while True:
    attempts += 1
    guess = safe_int_input("Enter your guess: ")
    if guess < secret_number:
        print("You guessed lower than the secret number")
    elif guess > secret_number:
        print("You guessed higher than the secret number")
    else:
        print(f"You got the number!! \nYou have attempted {attempts} times to get the number.")
        break

    if attempts >= max_attempt:
        print(f"\n\nYou have hit the maximum attempt!\nThe secret number was {secret_number} \nTry again!\n")
        break