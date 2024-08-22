import random
user_score = 0
comp_score = 0
options = ["rock","paper","scissor"]
while True:
    comp_no = random.randint(0,2)
    comp_choice = options[comp_no]
    user_choice = input("Type rock/paper/scissor or q to quit : \n")
    user_choice = user_choice.lower()
    if user_choice == 'q':
        break
    if user_choice not in options:
        print("Invalid Input")
        continue
    elif user_choice == "rock" and comp_choice == "scissor":
        print("You win")
        user_score += 1
    elif user_choice == "paper" and comp_choice == "rock":
        print("You win")
        user_score += 1
    elif user_choice == "scissor" and comp_choice == "paper":
        print("You won")
        user_score += 1
    elif user_choice == comp_choice :
        print("It's a draw")
    else:
        print("You lost")
        comp_score += 1
print(f"You won {user_score} times")
print(f"computer won {comp_score} times")
print("GoodBye !!")
