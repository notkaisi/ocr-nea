import tkinter as tk
import random

root = tk.Tk()
root.title('Game')

root_width = 600
root_height = 400

canvas = tk.Canvas(root, width=root_width, height=root_height, bg='white')
canvas.pack()

# The sprite is ALWAYS drawn at the center
sprite_size = 20
sprite = canvas.create_oval(
    root_width/2 - sprite_size/2,
    root_height/2 - sprite_size/2,
    root_width/2 + sprite_size/2,
    root_height/2 + sprite_size/2,
    fill='black'
)

def spawnEnemies():
    global ranx, rany
    numEnemies=random.randint(0,3)
    for i in range(numEnemies):
        ranx = random.randint(-300, 300)
        rany = random.randint(-200, 200)
        opp = canvas.create_oval(
            root_width/2 + ranx,
            root_height/2 + rany,
            root_width/2 + ranx + 50,
            root_height/2 + rany + 50,
            fill='red'
        )

speed = 5
keys_pressed = set()


def move_world(dx, dy):
    #Moves everything except the sprite.
    for item in canvas.find_all():
        if item != sprite:   # don't move the player
            canvas.move(item, dx, dy)

def move():
    global ranx, rany
    dx = 0
    dy = 0
    # player presses keys -> world moves in opposite direction
    if "a" in keys_pressed: 
        dx += speed    # move world right
        spawnEnemies()
    if "d" in keys_pressed: 
        dx -= speed    # move world left
    if "w" in keys_pressed: 
        dy += speed    # move world down
    if "s" in keys_pressed: 
        dy -= speed    # move world up
    if dx != 0 or dy != 0:
        move_world(dx, dy)
        ranx += dx
        rany += dy
    #make sure player is always centered
    player_x = root_width/2
    player_y = root_height/2
    if ranx < 0 < ranx + 50 and rany < 0 < rany + 50:
        start_battle()
    root.after(20, move)

#-------keybinds---------

def key_down(event):
    keys_pressed.add(event.keysym.lower())

def key_up(event):
    keys_pressed.discard(event.keysym.lower())

root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)


def start_battle():
    canvas.configure(bg='black')
    canvas.itemconfig(sprite, fill='white')
    #start battle

move()
root.mainloop()
