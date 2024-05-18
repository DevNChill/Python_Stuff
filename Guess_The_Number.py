import random
top_no = input("Type a number :")
if top_no.isdigit() :
    top_no = int(top_no)
    if top_no <= 0:
        print("Type a number greater than 0 next time")
        quit
else:
    print("Type a number next time")
    quit()
random_no = random.randint(0,top_no)
guess = 0
while True:
    guess += 1
    user_guess = input("Make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue
    if user_guess == random_no:
        print("The Number was", random_no )
        print(f"You guessed the number in {guess} times")
        break
    elif user_guess > random_no:
        print("Make a lower guess")
    else:
        print("Make a higher guess")
print("Game Over")
