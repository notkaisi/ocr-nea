import tkinter as tk
import time
import random
root=tk.Tk()
root.title('Battle')
#root.resizable(False, False)
canvas=tk.Canvas(root, width=600, height=400, bg='black')
canvas.pack()

def attack():
    damage=random.randint(0,100)
    if damage>10:
        text=canvas.create_text(300,200, text='You did '+str(damage)+' dmg!', font=('Comic Sans', 50), fill='red')
        # remove text after 2 seconds (2000 ms)
        canvas.after(1000, lambda: canvas.delete(text))
    else:
        text=canvas.create_text(300,200, text='You missed!', font=('Comic Sans', 50), fill='red')
        canvas.after(1000, lambda: canvas.delete(text))
        #print('You did ',random.randint(1,100),' dmg!')
def skill():
    print('You have a skill issue')

start_button = tk.Button(canvas, text="Attack", font=("Arial", 18), command=attack)
start_button.pack(pady=40)

# Place button on the canvas
canvas.create_window(300, 350, window=start_button)
#exit button
exit_button = tk.Button(canvas, text="Skill", font=("Arial", 18), command=skill)
exit_button.pack(pady=20)
canvas.create_window(400, 350, window=exit_button)

damage=random.randint(0,100)
root.mainloop()
