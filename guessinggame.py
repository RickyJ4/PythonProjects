#Guess the number game no given hints of weather the number is higher or lower
import random

random_number = random.randint(1,20)

print('I am thinking of a Number between 1 and 20')
guessed = int(input('Can you guess which number i am thinking of : '))

attempts = 3
guesses = 0
while guesses < attempts:
    if(guessed != random_number):
        print('Incorrect try again ')
        guessed = int(input('Can you guess which number i am thinking of : '))
        guesses += 1
    elif (random_number == guessed):
        print('You guessed my Number Congradulations !!')

print('Unfortunately you have run out of attempts')
   
    
        


