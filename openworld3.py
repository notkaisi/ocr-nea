print("MENU FILE STARTED")

import tkinter as tk
import random
import time
import math

root = tk.Tk()
root.title('Game')

root_width = 600
root_height = 400

canvas = tk.Canvas(root, width=root_width, height=root_height, bg='white')
canvas.pack()

#---sprite at center
sprite_size = 20
sprite = canvas.create_oval(
    root_width/2 - sprite_size/2,
    root_height/2 - sprite_size/2,
    root_width/2 + sprite_size/2,
    root_height/2 + sprite_size/2,
    fill='black'
)

speed = 5
keys_pressed = set()

enemies = []  #--store enemy IDs

def spawnEnemies():
    numEnemies = random.randint(1, 3)
    MARGIN = 50  # spawn just off-screen

    for _ in range(numEnemies):
        side = random.randint(0, 3)

        if side == 0:      # LEFT
            x = -MARGIN
            y = random.randint(0, root_height)
        elif side == 1:    # RIGHT
            x = root_width + MARGIN
            y = random.randint(0, root_height)
        elif side == 2:    # TOP
            x = random.randint(0, root_width)
            y = -MARGIN
        else:              # BOTTOM
            x = random.randint(0, root_width)
            y = root_height + MARGIN

        enemy = canvas.create_oval(
            x, y,
            x + 40, y + 40,
            fill="red"
        )

        enemies.append(enemy)

world_x = 0
world_y = 0
player_world_x = 0
player_world_y = 0

def move_world(dx, dy):
    global world_x, world_y
    # move everything except player
    for item in canvas.find_all():
        if item != sprite:
            canvas.move(item, dx, dy)
    world_x += -dx
    world_y += -dy

chunk_size = 400
visited_chunks = set()

def get_current_chunk():
    cx = int(player_world_x // chunk_size)
    cy = int(player_world_y // chunk_size)
    return (cx, cy)

def check_collisions():
    px1, py1, px2, py2 = canvas.coords(sprite)
    for enemy in enemies:
        ex1, ey1, ex2, ey2 = canvas.coords(enemy)

        overlap = not (px2 < ex1 or px1 > ex2 or py2 < ey1 or py1 > ey2)
        if overlap:
            start_battle()
            return

def move():
    global player_world_x, player_world_y

    dx = dy = 0

    if "a" in keys_pressed:
        dx += speed
    if "d" in keys_pressed:
        dx -= speed
    if "w" in keys_pressed:
        dy += speed
    if "s" in keys_pressed:
        dy -= speed

    if dx != 0 or dy != 0:
        move_world(dx, dy)

        #---update world coords
        player_world_x += -dx
        player_world_y += -dy

        #---check chunk----
        chunk = get_current_chunk()
        if chunk not in visited_chunks:
            visited_chunks.add(chunk)
            spawnEnemies()

    check_collisions()
    root.after(20, move)

#------keybinds------
def key_down(event):
    keys_pressed.add(event.keysym.lower())

def key_up(event):
    keys_pressed.discard(event.keysym.lower())

root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

def start_battle():
    canvas.configure(bg='black')
    canvas.itemconfig(sprite, fill='white')
    print("Battle started!")

move()
root.mainloop()

