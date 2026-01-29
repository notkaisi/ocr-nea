import tkinter as tk
import random
root = tk.Tk()
root.title('Game')

root_width = 600
root_height = 400

canvas = tk.Canvas(root, width=root_width, height=root_height, bg='white')
canvas.pack()

sprite = canvas.create_oval(290, 180, 310, 200, fill='black')

#opp_width = random.randint(100,500)
#opp_height=random.randint(50,300)
#opp = canvas.create_oval(opp_height,opp_width+75, opp_width, opp_height+60)
ranx=random.randint(0,550)
rany=random.randint(0,350)
print(ranx, rany)
#opp = canvas.create_oval(10+ranx, 10+rany, 40+ranx, 40+rany, fill='green')
opp = canvas.create_oval(0+ranx,0+rany,50+ranx,50+rany, fill='green')
speed = 5   # smooth speed

keys_pressed = set()   # track which keys are held
def move():
    """Smooth continuous movement loop."""
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

    # Call this function again 16 ms later (~60 FPS)
    root.after(30, move)
def key_down(event):
    keys_pressed.add(event.keysym.lower())
def key_up(event):
    if event.keysym in keys_pressed:
        keys_pressed.remove(event.keysym.lower())


root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

move()  # start the movement loop
root.mainloop()
