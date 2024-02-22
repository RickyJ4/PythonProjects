import random

team_A = input('Enter the name of first team : ')
team_B = input('Enter the name of second team : ')

selection = input(team_A +  'Would you like to bat or bowl : ')

coin_toss = random.randint(0,1)
if (coin_toss == 1):
    print(' After coin toss' + team_A  + 'is to bowl first')
else:
    print(' After coin toss' + team_A  + 'is to bat first')

balls = 60
runs = [0, 1 , 2 , 3 , 4 , 5 , 6 ]

def inning():
    score = 0
    for _ in range(balls):
        run = random.choice(runs)
        if run == 5:
            print('Wide run + 4 runs')
        else:
            
            print(f"You scored {run} runs ")
        score += run 
    return score

team_a_score = inning()
team_b_score = inning()

total_team_a = f'Total score for {team_A} is {team_a_score}'
print(f'{team_A} total score {team_a_score}')
total_team_b = f'Total score for {team_B} is {team_b_score}'
print(f'{team_B} total score {team_b_score}')

if total_team_a > total_team_b:
    print(f'{team_A} won ')
else:
    print(f'{team_B} won')
    







