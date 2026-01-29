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
    if damage>10 and damage<90:
        text=canvas.create_text(300,200, text='You did '+str(damage)+' dmg!', font=('Comic Sans', 50), fill='white')
        # remove text after 2 seconds (2000 ms)
        canvas.after(1000, lambda: canvas.delete(text))
    elif damage>=90:
        text=canvas.create_text(300,200, text='''You did '''+str(damage*2)+''' dmg! 
           It was a CRITICAL HIT!''', font=('Comic Sans', 30), fill='yellow')
        # remove text after 2 seconds (2000 ms)
        canvas.after(1000, lambda: canvas.delete(text))
    else:
        damage=0
        text=canvas.create_text(300,200, text='You missed!', font=('Comic Sans', 50), fill='red')
        canvas.after(1000, lambda: canvas.delete(text))
        #print('You did ',random.randint(1,100),' dmg!')
def skill():
    print('skill used')
    damage=random.randint(500,1000)
    if damage>550 and damage<900:
        text=canvas.create_text(300,200, text='You did '+str(damage)+' dmg!', font=('Comic Sans', 50), fill='white')
        # remove text after 2 seconds (2000 ms)
        canvas.after(1000, lambda: canvas.delete(text))
    elif damage>=900:
        text=canvas.create_text(300,200, text='''You did '''+str(damage*2)+''' dmg! 
           It was a CRITICAL HIT!''', font=('Comic Sans', 30), fill='yellow')
        # remove text after 2 seconds (2000 ms)
        canvas.after(1000, lambda: canvas.delete(text))
    else:
        damage=0
        text=canvas.create_text(300,200, text='You missed!', font=('Comic Sans', 50), fill='red')
        canvas.after(1000, lambda: canvas.delete(text))

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
