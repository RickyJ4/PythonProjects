# Simple Budgets Project 
import keyboard

#appending expenses into a list
recreational = []
fixed_costs = []
Grocery = []
amount = int(input('Enter amount you have : '))

#Adding expenses to the respective lists
print('Calculating Expenses...')
complete = False
while not complete:
    print('Which costs do you want to add')
    print('1: Recreational costs \n2: Fixed costs \n3: Groceries')
    options = input('Enter selection : ')
    print('Press 4 key when completed ')
    if(options == '1'):
        recreational_spending = int(input('Enter your recreational costs : '))
        recreational.append(recreational_spending)
    elif(options == '2'):
        fixed_spending = int(input('Enter your fixed costs : '))
        fixed_costs.append(fixed_spending)
    elif(options == '3'):
        Groceries = int(input('Enter your Grocery costs : '))
        Grocery.append(Groceries)
    else: 
        complete = True
#checking to see if list is being printed
print(recreational)
print(fixed_costs)
print(Grocery)


#adding up list totals 
recreational_total = sum(recreational)
fixed_total = sum(fixed_costs)
Grocery_total = sum(Grocery)

print(f'Money spent on Recreation = {recreational_total}, Groceries = {Grocery_total} and your fixed costs are {fixed_total}')
amount_left = amount - (recreational_total + fixed_total + Grocery_total)
print(f'Amount left is {amount_left}')
    
        
        
    




