import random
choice = input("Choose one paper, rock, or scissors: ")
print("You chose: " + choice)
computer = random.choice(["paper", "rock", "scissors"])
print("Computer: " + computer)
if choice == computer :
    print("It's a tie!")
elif choice == "paper" :
    if computer == "rock" :
        print("You win!")
    else :
        print("You lose!")
elif choice == "rock" :
    if computer == "scissors" :
        print("You win!")
    else :
        print("You lose!")
elif choice == "scissors" :
    if computer == "paper" :
        print("You win!")
    else :
        print("You lose!")