import os
import random#draw grid

#pick random location the player
#pick random location for the exit door
#pick random location for the monster
#draw a player in grid
#take input or movement

#move player , unless invalid move 
#check for win/lose
#clear screen and random grid

CELLS= [
    (0,0),(1,0),(2,0),(3,0),(4,0),
    (0,1),(1,1),(2,1),(3,1),(4,1),
    (0,2),(1,2),(2,2),(3,2),(4,2),
    (0,3),(1,3),(2,3),(3,3),(4,3),
    (0,4),(1,4),(2,4),(3,4),(4,4)
]
def clear_screen():
    os.system('cls' if os.name =='nt' else 'clear')
def get_locations():
    return random.sample(CELLS,3)



def move_player(player,move):
    #get the players location
    """if move left ,x-1
    if move right ,x+1
    if move up ,y-1 
    if move down ,y+1
    """
    x,y=player
    if move=='UP':
        y-=1
    
    if move=='DOWN':
        y+=1
    if move=='RIGHT':
        x+=1
    if move=='LEFT':
        x-=1
    
    return x,y

def get_move(player):
    moves=["LEFT","RIGHT","UP","DOWN"]
    
    x , y=player
    if x==0:
        moves.remove("LEFT")
    if x==4:
        moves.remove("RIGHT")
    
    if y==0:
        moves.remove("UP")
    
    if y==4:
        moves.remove("DOWN")
    
    return moves
    """if player's y==0,they can't move up
    if player's y==4,they can't move down
    if player's x==0,they can't move left
    if player's x==4,they can't move right
    
    """
def draw_map(player):
    print(" _"*5)
    tile="|{}"
    for cell in CELLS:
        x,y=cell
        if x<4:
            line_end=""
            if cell==player:
                output=tile.format("X")
            else:
                output=tile.format("_")
        else:
            line_end="\n"
            if cell==player:
                output=tile.format("X|")
            else:
                output=tile.format("_|")
        print(output,end=line_end)
                
            
        
    
def game_loop():
    monster,door,player=get_locations()
    
    playing=True
    while playing:
        clear_screen()
        
        draw_map(player)
        valid_moves=get_move(player)
        
        print("you are currenly in room {}".format(player))  
        print("You can move {}".format(",".join(valid_moves))) 
        print("ENTER QUIT to quit.")
        
        move=input("> ")
        move=move.upper()
        
        if move =='QUIT':
            break
        
        if move in valid_moves:
            player=move_player(player,move)
            
            if player==monster:
                print("\n  ** OH NO !the monster got you! Better Luck next time! **\n")
                playing=False
            
            if player==door:
                print("\n  ** You escaped the dungeon! **\n")
                playing=False
            
            
        else:
            input("\n * * Walls are Hard ! Dont run into them ** \n")
        
        
    
    else:
        if input('Play again? [Y/n]').lower()!="n":
            game_loop()
clear_screen()
print("Welcome to the dungeon!")
input("press 'return to start!")
clear_screen()
game_loop()
