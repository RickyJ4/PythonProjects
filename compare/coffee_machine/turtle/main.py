#from turtle import Turtle,Screen

#law = Turtle()
#print(law)

#law.shape("turtle")
#law.color("cyan")
#law.forward(200)

#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu,Squirtle,Charmander"])
table.add_column("Type", ["Electric,Water,Fire"])
table.align = "§1"
print(table)
