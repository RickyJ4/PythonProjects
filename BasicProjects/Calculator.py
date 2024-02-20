
operations = ['*','+','/','-']

num_1 = int(input('Enter Number 1 : '))
num_2 = int(input('Enter Number 2 : '))
    
for i in operations:
    print(i)
opp = input('Select operation : ')

if opp == '*':
    print(num_1 * num_2)
elif opp == '+':
    print(num_1 + num_2)
elif opp == '/':
    print(num_1/num_2)
else:
    print(num_1-num_2)





