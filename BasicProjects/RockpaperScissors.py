import random

print('Lets play rock paper scissors')

options = ['rock', 'paper', 'scissors']


user_score = 0
computer_score = 0
attempts = 0
#checking to see who won best of 3
while attempts < 3:
    user_choice = input('rock, paper or scissors : ')
    computer_choice = random.choice(options)
    if(user_choice == 'rock' and computer_choice =='scissors' or user_choice == 'paper' and computer_choice =='rock' or user_choice == 'scissors' and computer_choice =='paper'):
        print('User wins round')
        user_score += 1
    else:
        print('Computer wins round')
        computer_score +=1
    
    attempts += 1

#Displaying winner 
if(user_score > computer_score):
    print(f'User wins {user_score} to {computer_score}')
else:
    print(f'Computer wins {computer_score} to {user_score}')


    





