import tkinter as tk
import time
import random
root=tk.Tk()
root.title('Menu')
#root.resizable(False, False)
canvas=tk.Canvas(root, width=600, height=400, bg='pink')
canvas.pack()

text = canvas.create_text(300, 200, text='Game', font=('Arial', 40), fill='black')
def start():
    print('game started')
def exit():
    print('game exited')
start_button = tk.Button(canvas, text="start", font=("Arial", 18), command=start)
start_button.pack(pady=40)

# Place button on the canvas
canvas.create_window(300, 350, window=start_button)
#exit button
exit_button = tk.Button(canvas, text="exit", font=("Arial", 18), command=exit)
exit_button.pack(pady=20)
canvas.create_window(550, 50, window=exit_button)

root.mainloop()
