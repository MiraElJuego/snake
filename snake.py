import os
import random 

import readchar 

os.system('clear')

POSITION_X = 0
POSITION_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUMBER_OF_ENEMIES = 20

tail_lenght = 0

enemies = []

current_position = [3, 1]

while len(enemies) < NUMBER_OF_ENEMIES:
    position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
    if position not in enemies and position != current_position:
        enemies.append(position)    

while True:
    print("+"+"-"*(MAP_WIDTH*3)+"+\r")
    for cordinate_y in range(MAP_HEIGHT):    
        print("|", end="")
        for cordinate_x in range(MAP_WIDTH):
            character = "···"
            object_in_position = None
            for enemy in enemies:
                if cordinate_x == enemy[POSITION_X] and cordinate_y == enemy[POSITION_Y]:
                    character = "·$·"
                    object_in_position = enemy

            if cordinate_x == current_position[POSITION_X] and cordinate_y == current_position[POSITION_Y]:
                if object_in_position:
                    enemies.remove(object_in_position)
                    tail_lenght += 1
                character = "·@·"
            
            print(character, end="")
        print("|\r")       
    print("+"+"-"*(MAP_WIDTH*3)+"+\r")
    print("Tamaño de la cola: "+str(tail_lenght)+"\r")

    direction = readchar.readchar()

    if direction == "w":
        current_position[POSITION_Y] -= 1
        current_position[POSITION_Y] %= MAP_HEIGHT
    elif direction == "s":
        current_position[POSITION_Y] += 1
        current_position[POSITION_Y] %= MAP_HEIGHT
    elif direction == "a":
        current_position[POSITION_X] -= 1
        current_position[POSITION_X] %= MAP_WIDTH
    elif direction == "d":
        current_position[POSITION_X] += 1
        current_position[POSITION_X] %= MAP_WIDTH
    elif direction == "q":
        break    


    os.system("clear")
