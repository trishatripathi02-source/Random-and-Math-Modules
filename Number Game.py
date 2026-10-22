import random
playing = True
number = str(random.randint(0, 15))

print("I will be generating a number from 0 to 15 and you have to guess my number!")
print("The game will end if you get 1 hero. So be wise with your guessing!")

while playing:
    guess = input("Give me your Guess here!")
    if number == guess:
        print("You won!")
        print(f"The number was {number}\n")
        break

    else:
        print("Your guess isn't correct. Let's try a second time!")
        