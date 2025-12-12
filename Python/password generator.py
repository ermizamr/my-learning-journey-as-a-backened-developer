import random
import string
from datetime import datetime

print("choose password strength:")
print("1. Easy (letters only)")
print("2. Strong (Letters + numbers)")
print("3. Hard (Letters + numbers + symbols)")

choice = int(input("please choose your desired password style: "))
length = int(input("what length of password would you prefer: "))

upper = string.ascii_uppercase
lower = string.ascii_lowercase
numbers = string.digits
symbol = string.punctuation

if choice == 1:
    character = upper + lower
    required = [random.choice(upper), random.choice(lower)]

elif choice == 2:
    character = upper + lower + numbers
    required = [random.choice(upper), random.choice(lower), random.choice(numbers)]

else:
    character = upper + lower + numbers + symbol
    required = [random.choice(upper), random.choice(lower), random.choice(numbers), random.choice(symbol)]

remaining_length = length-len(required)
password = required + [random.choice(character) for i in range(remaining_length)]
random.shuffle(password)

password = "".join(password)

print("Your password is: ", password)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
entry = f"{timestamp} - {password}"

with open("generated_password.txt", "a") as file:
    file.write(entry)

print("password saved succesfully!")