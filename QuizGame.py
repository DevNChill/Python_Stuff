print("welcome to my computer quiz")
choice = input("wanna play (y/n)")
score=0
if choice != 'y':
    print('better luck next time')
    quit()
else:
    print('get ready to play the game ?')
question1 = 'What is the full form of CPU ?'
question2 = 'What is the full form of GPU  ?'
question3 = 'What is the full form of IP address ?'
question4 = 'What is the full form of ssh ?'
question5 = 'What is the default port for ssh ?'
question6 = 'What is the full form of http ?'
question7 = 'What is the full form of FTP ?'
question8 = 'What is the default port for FTP ?'
question9 = 'Which username is used to log into ftp without password ?'
question10 = 'What is the full form of TCP ?'
print (question1)
answer = input().lower()
if answer == 'central processing unit':
    print('Correct !')
    score+=1
else:
    print('Incorrect !')
print (question2)
answer = input().lower()
if answer == 'graphical processing unit':
    print('Correct !')
    score+=1
else:
    print('Incorrect !')
print (question3)
answer = input().lower()
if answer == 'internet protocol address':
    print('Correct !')
    score+=1
else:
    print('Incorrect !')
print (question4)
answer = input().lower()
if answer == 'secure shell':
    print('Correct !')
    score+=1
else:
    print('Incorrect !')
print (question5)
answer = input().lower()
if answer == '22':
    print('Correct !')
    score+=1
else:
    print('Incorrect !')
print (question6)
answer = input().lower()
if answer == 'hyper text transfer protocol':
    print('Correct !')
    score+=1
else:
    print('Incorrect !')
print (question7)
answer = input().lower()
if answer == '21':
    print('Correct !')
    score+=1
else:
    print('Incorrect !')
print (question8)
answer = input().lower()
if answer == 'file transfer protocol':
    print('Correct !')
    score+=1
else:
    print('Incorrect !')
print (question9)
answer = input().lower()
if answer == 'anonnymous':
    print('Correct !')
    score+=1
else:
    print('Incorrect !')
print (question10)
answer = input().lower()
if answer == 'transmission control protocol':
    print('Correct !')
    score+=1
else:
    print('Incorrect !')
print(f'You scored {score} out of 10 points ')
print("Thanks for playing this game")

