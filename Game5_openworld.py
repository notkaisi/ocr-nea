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

# Player sprite at center
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

enemies = []  # <-- store enemy IDs here

def spawnEnemies():
    numEnemies = random.randint(0, 3)
    for i in range(numEnemies):
        ranx = random.randint(-300, 300)
        rany = random.randint(-200, 200)
        enemy = canvas.create_oval(
            root_width/2 + ranx,
            root_height/2 + rany,
            root_width/2 + ranx + 50,
            root_height/2 + rany + 50,
            fill='red'
            )
        enemies.append(enemy)  # store the ID


def move_world(dx, dy):
    # move everything except the player
    for item in canvas.find_all():
        if item != sprite:
            canvas.move(item, dx, dy)

def check_collisions():
    px1, py1, px2, py2 = canvas.coords(sprite)
    for enemy in enemies:
        ex1, ey1, ex2, ey2 = canvas.coords(enemy)

        overlap = not (px2 < ex1 or px1 > ex2 or py2 < ey1 or py1 > ey2)
        if overlap:
            start_battle()
            return

max_distance=400
def enemies_far_enough():
    #return True if all enemies are outside the required spawn distance.
    px = root_width / 2
    py = root_height / 2
    for enemy in enemies:
        ex1, ey1, ex2, ey2 = canvas.coords(enemy)
        ex = (ex1 + ex2) / 2
        ey = (ey1 + ey2) / 2

        dist = math.hypot(ex - px, ey - py)
        if dist < max_distance:
            return False
    return True
def move():
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
        if enemies_far_enough():
            spawnEnemies()

    check_collisions()

    root.after(20, move)

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
