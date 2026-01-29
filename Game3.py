import tkinter as tk
import random
root = tk.Tk()
root.title('Game')

root_width = 600
root_height = 400

canvas = tk.Canvas(root, width=root_width, height=root_height, bg='white')
canvas.pack()

sprite = canvas.create_oval(290, 180, 310, 200, fill='black')

ranx=random.randint(0,550)
rany=random.randint(0,350)
print(ranx, rany)
opp = canvas.create_oval(ranx,rany,50+ranx,50+rany, fill='green')
speed = 5   # smooth speed

keys_pressed = set()   # track which keys are held
def move():
    x1, y1, x2, y2 = canvas.coords(sprite)

    # move left & right
    if "a" in keys_pressed and x1 - speed >= 0:
        canvas.move(sprite, -speed, 0)
    if "d" in keys_pressed and x2 + speed <= root_width:
        canvas.move(sprite, speed, 0)
    # move up & down
    if "w" in keys_pressed and y1 - speed >= 0:
        canvas.move(sprite, 0, -speed)
    if "s" in keys_pressed and y2 + speed <= root_height:
        canvas.move(sprite, 0, speed)

    x1, y1, x2, y2 = canvas.coords(sprite)
    centre_x = (x1 + x2) / 2
    centre_y = (y1 + y2) / 2
    #sprite_pos=centre_x, centre_y
    #print("sprite position:",sprite_pos)
    if centre_x>ranx and centre_x<50+ranx and centre_y>rany and centre_y<50+rany:
        print('battle commenced')
        start(root, canvas, sprite)
    root.after(30, move)
def key_down(event):
    keys_pressed.add(event.keysym.lower())
def key_up(event):
    if event.keysym in keys_pressed:
        keys_pressed.remove(event.keysym.lower())

def start(root, canvas, sprite):
    canvas.configure(bg='black')
    canvas.itemconfig(sprite, fill='white')
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)


move()  # start the movement loop
print('started')
root.mainloop()
