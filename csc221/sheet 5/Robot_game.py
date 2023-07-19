from gasp import *

begin_graphics()
c = Circle((320, 200), 5)
move_to(c, (350,220))
from random import randint
num1=(0,63)
num2=(0, 47)
player_x= num1
player_y= num2
Circle((10 * player_x + 5, 10 * player_y +5), 5, filled= True)
finished = False 
def place_player():
print ("I'm right here!")
move_player():
print("I'm moving to...")
update_when ("Key_pressed")

finished = False
def place_player_(x):
    print("I'm right here!")
def move_player():
    print("I'm moving...")
    update_when('key_pressed')

while not finished:
    move_player()

    end_graphics()