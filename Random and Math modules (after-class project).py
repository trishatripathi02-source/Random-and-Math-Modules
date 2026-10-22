# Step 1: Import modules
import random
import math

# Step 2: Generate a lucky number
lucky_number = random.randint(1, 10)
print("Your lucky number is:", lucky_number)

# Step 3: Choose a random activity
fun_choices = [
    "Read a book",
    "Go for a walk",
    "Listen to music",
    "Watch a movie",
    "Play a game"
]

activity = random.choice(fun_choices)
print("Today's activity:", activity)

# Step 4: Build the guessing game
secret_number = random.randint(1, 5)

print("\nGuess the secret number between 1 and 5!")

while True:
    guess = int(input("Enter your guess: "))

    # Step 5: Stop the guessing loop
    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        break
    else:
        print("Wrong guess. Try again!")

# Step 6: Use ceil() and floor()
decimal_num = float(input("\nEnter a decimal number: "))
print("Rounded up (ceil):", math.ceil(decimal_num))
print("Rounded down (floor):", math.floor(decimal_num))

# Step 7: Use copysign() and fabs()
x = float(input("\nEnter the first number: "))
y = float(input("Enter the second number: "))

print("copysign(x, y):", math.copysign(x, y))
print("Absolute value of x:", math.fabs(x))

# Step 8: Use gcd()
num1 = int(input("\nEnter the first integer: "))
num2 = int(input("Enter the second integer: "))

print("Greatest Common Divisor (GCD):", math.gcd(num1, num2))

# Step 9: End message
print("\nRun the program again to see different lucky numbers,")
print("activities, and secret numbers!")