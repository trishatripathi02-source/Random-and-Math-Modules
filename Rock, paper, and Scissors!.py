import random 

while True:
    my_choice = input("enter your choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_actions)
    print(f"You chose {my_choice}, the computer chose {computer_choice}\n")

    if my_choice == computer_choice:
        print(f"Both of you selected {my_choice}. It's a draw!\n")
    elif my_choice == "rock":
        if computer_choice == "scissors":
            print("Rock breaks scissors! You win!")
        else: 
            print("Paper covers rock! you lost!")
    elif my_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! you win!")
        else:
            print("Scissors cuts paper! You lost!")
    elif my_choice == "scissors":
       if computer_choice == "paper":
           print("Scissors cuts paper! You win!")
       else:
           print("Rock breaks scissors! You lose!")

           play_again = input("Want to play again? (y/n): ")
           if play_again != "y":
               break