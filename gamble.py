import random



print("This game requires 2 players ")
print("Please enter your usernames respectively")
user_1_name = input("name for user_1 : \n")
user_2_name = input("name for user_2 : \n")

# user inputs and scores
user1_score = 0
user2_score = 0
user1_input = ''
user2_input = ''


# rolling the dice 
def roll():
    dice_no = random.randrange(1,6)
    return dice_no

dice_no = roll()



# gambling starts
while True:
    user1_input = input(f"{user_1_name}'s turn | press 'r' to roll the dice  | q to quit :")
    user1_input = user1_input.lower()
    if user1_input == 'r':
        dice_no = roll()
        print(f"the no for {user_1_name}'s is {dice_no}")
        if dice_no == 1:
            user1_score = 0
            print(f"{user_1_name}'s score is reset to 0")
        else:
            user1_score = user1_score + dice_no
            print(f"{user_1_name}'s current score is {user1_score}")
        if user1_score == 50:
            print('Hooray ! you won')
            quit()
        else:
            pass
    else:
        print(f"{user_1_name}'s score is {user1_score}")
        print("See you next time !")
        quit()

    user2_input = input(f"{user_2_name}'s turn | press 'r' to roll the dice  | 'q' to quit :")
    user2_input = user2_input.lower()
    if user2_input == 'r':
        dice_no = roll()
        print(f"the no for {user_2_name}'s is {dice_no}")
        if dice_no == 1:
            user1_score = 0
            print("{user_2_name}'s score is reset to 0")
        else:
            user2_score = user2_score + dice_no
            print(f"{user_2_name}'s current score is {user2_score}")

        if user2_score == 50:
            print('Hooray ! you won')
            quit()
        else:
            pass
    else:
        print(f"{user_2_name}'s  is {user2_score}")
        print("See you next time !")
        quit()