import random

user_score  = 0
computer_score = 0
choise_list = ["paper", "rock", "scissors"]

while True:
    user_input = input("Type (paper/rock/scissors) or (q to quit): ").lower()
    
    if user_input == 'q':
        break
    
    if user_input not in choise_list:
        print("Enter valid option")
        continue

    random_number = random.randint(0,2)

    computer_pick = choise_list[random_number]
    print(f"Computer Picked: {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("user won!")
        user_score+=1
    
    elif user_input == "rock" and computer_pick == "paper":
        print("Computer Won!")
        computer_score+=1

    elif user_input == "paper" and computer_pick == "scissors":
        print("Computer Won!")
        computer_score +=1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_score +=1

    elif user_input == "scissors" and computer_pick == "rock":
        print("Computer Won!")
        computer_score +=1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_score +=1
    
    else:
        print("Equal")

print("Game Ended")
print(f"Your Score {user_score} points.")
print(f"Computer Score {computer_score} points.")