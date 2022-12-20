#Created instructions for Player

def show_instructions():  
   #print a main menu and the commands
   print("*********Adventure Game*************\n")
   print("Move commands: South, North, East, West,Exit\n")
   print("*************************************")

show_instructions()
#Created Blueprint for Game Area and Rewards
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    } 
#Created Blueprint for Game Area and Rewards
import random
position=random.randint(1,3)

if position==1:
    Player='Great Hall'
elif position==2:
    Player='Bedroom'
elif position==3:
    Player='Cellar'
#Game will run untill Exit

i=0
while i<=100:
    print('You are in the {0}'.format(Player))
    
    print("Enter your move:")
    Move=input()
    Room_details=rooms[Player]
    if Move=='Exit':#check for Exit
        print('You Exit from Game!')
        break
    if Move in Room_details:#Check valid Move
        Player=Room_details[Move]
    else:
        print('Invalid move!,Try another Move')
    i=i+1