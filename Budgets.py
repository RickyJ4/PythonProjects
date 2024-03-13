import keyboard

# Simple Budgets Project 

#appending expenses into a list
recreational_costs= []
fixed_costs = []
Grocery = []
amount = input('Enter amount you have : ')

# 
print('Calculating Expenses...')
complete = False
while not complete:
    print('Which costs do you want to add')
    print('1: Recreational costs \n2: Fixed costs \n3: Groceries')
    options = input('Enter selection : ')
    print('Press D key when completed ')
    if(options == '1'):
        recreational_spending = int(input('Enter your recreational costs : '))
        recreational_costs.append(recreational_costs)
    elif(options == '2'):
        fixed_spending = int(input('Enter your fixed costs : '))
        fixed_costs.append(fixed_spending)
    else:
        Groceries = input('Enter your Grocery costs : ')
        Grocery.append(Groceries)

    if keyboard.is_pressed('d'):
        complete = True

recreational_total = 0
for i in range(recreational_costs):
    recreational_total += i
fixed_total = 0
for i in range(fixed_costs):
    fixed_total += i
Grocery_total = 0
for i in range(Grocery):
    Grocery_total += i

print(f'Money spent on Recreation = {recreational_total}, Groceries = {Grocery_total} and your fixed costs are {fixed_total}')
amount_left = amount - (recreational_total + fixed_total + Grocery_total)
print(f'Amount left is {amount_left}')
    
        
        
    




