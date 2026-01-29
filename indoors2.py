import tkinter as tk
import random

root = tk.Tk()
root.title('Game')
root_width = 600
root_height = 400

canvas = tk.Canvas(root, width=root_width, height=root_height, bg='white')
canvas.pack()

sprite = canvas.create_oval(290, 180, 310, 200, fill='black')

ranx = random.randint(0, 550)
rany = random.randint(0, 350)
opp = canvas.create_oval(ranx, rany, 50 + ranx, 50 + rany, fill='green')

speed = 5  # smooth speed
keys_pressed = set()  # track which keys are held

# Initialize player's center position
centre_x, centre_y = 290 + 10, 180 + 10  # initial center of the sprite

# List to store obstacles (rectangles)
obstacles = []

def move():
    dx = dy = 0
    x1, y1, x2, y2 = canvas.coords(sprite)
    if "a" in keys_pressed and x1 - speed >= 0:
        dx = -speed
    if "d" in keys_pressed and x2 + speed <= root_width:
        dx = speed
    if "w" in keys_pressed and y1 - speed >= 0:
        dy = -speed
    if "s" in keys_pressed and y2 + speed <= root_height:
        dy = speed
    canvas.move(sprite, dx, dy)
    if touching(sprite, opp):
        start(root, canvas, sprite)
        return  # stop movement loop 

    for obj in obstacles:
        if touching(sprite, obj):
            canvas.move(sprite, -dx, -dy)

    root.after(30, move)

def spawn_objects():
    # Spawn new obstacle (rectangle)
    ranx = random.randint(0, 550)
    rany = random.randint(0, 350)
    object1 = canvas.create_rectangle(ranx, rany, 50 + ranx, 50 + rany, fill='brown')
    obstacles.append(object1)

def check_collision(px, py, obj):
    # Check if the player collides with a given object (obstacle)
    ox1, oy1, ox2, oy2 = canvas.coords(obj)
    return ox1 < px < ox2 and oy1 < py < oy2
def touching(a, b):
    ax1, ay1, ax2, ay2 = canvas.coords(a)
    bx1, by1, bx2, by2 = canvas.coords(b)

    return not (ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2)
def key_down(event):
    keys_pressed.add(event.keysym.lower())

def key_up(event):
    if event.keysym in keys_pressed:
        keys_pressed.remove(event.keysym.lower())

def start(root, canvas, sprite):
    canvas.configure(bg='black')
    canvas.itemconfig(sprite, fill='white')
    # You can add battle mechanics or other game events here
    print("Battle started!")

root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

for i in range(2):
    spawn_objects()

# Start the movement loop
move()
print('Game started')

root.mainloop()
