import tkinter as tk

root = tk.Tk()
root.title('Game')

root_width = 600
root_height = 400

canvas = tk.Canvas(root, width=root_width, height=root_height, bg='white')
canvas.pack()

sprite = canvas.create_oval(290, 180, 310, 200, fill='black')
sprite_dx = 15
sprite_dy = 15

speed = 5   # smooth speed
keys_pressed = set()   # track which keys are held

def move():
    """Smooth continuous movement loop."""
    x1, y1, x2, y2 = canvas.coords(sprite)

    # Move left
    if "a" in keys_pressed and x1 - speed >= 0:
        canvas.move(sprite, -speed, 0)

    # Move right
    if "d" in keys_pressed and x2 + speed <= root_width:
        canvas.move(sprite, speed, 0)

    # Move up
    if "w" in keys_pressed and y1 - speed >= 0:
        canvas.move(sprite, 0, -speed)

    # Move down
    if "s" in keys_pressed and y2 + speed <= root_height:
        canvas.move(sprite, 0, speed)

    # Call this function again 16 ms later (~60 FPS)
    root.after(30, move)


def key_down(event):
    keys_pressed.add(event.keysym)


def key_up(event):
    if event.keysym in keys_pressed:
        keys_pressed.remove(event.keysym)


root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

move()  # start the movement loop
root.mainloop()
