import tkinter as tk
import time
import random
root=tk.Tk()
root.title('Battle')
#root.resizable(False, False)
canvas=tk.Canvas(root, width=600, height=400, bg='black')
canvas.pack()

enemy_hp = 5000   #global HP

def attack():
    global enemy_hp
    damage = random.randint(0, 100)

    if 10 < damage < 90:
        text = canvas.create_text(300, 200,text="You did " + str(damage) + " dmg!",font=('Comic Sans', 50),fill='white')
        canvas.after(1000, lambda: canvas.delete(text))
        damage(enemy_hp) #this dont work

    elif damage >= 90:
        text = canvas.create_text(300, 200,text="You did " + str(damage * 2) + " dmg!\nCRITICAL HIT!",font=('Comic Sans', 30),fill='yellow')
        canvas.after(500, lambda: canvas.delete(text))
        damage(enemy_hp)

    else:
        text = canvas.create_text(300, 200,text="You missed!",font=('Comic Sans', 50),fill='red')
        canvas.after(1000, lambda: canvas.delete(text))
        damage(enemy_hp)


def skill():
    global enemy_hp
    print("Skill used")

    damage = random.randint(500, 1000)

    if 550 < damage < 900:
        text = canvas.create_text(300, 200,text="You did " + str(damage) + " dmg!",font=('Comic Sans', 50),fill='white')
        canvas.after(1000, lambda: canvas.delete(text))
        damage(enemy_hp)

    elif damage >= 900:
        text = canvas.create_text(
            300, 200,
            text="You did " + str(damage * 2) + " dmg!\nCRITICAL HIT!",
            font=('Comic Sans', 30),
            fill='yellow'
        )
        canvas.after(1000, lambda: canvas.delete(text))
        damage(enemy_hp)

    else:
        text = canvas.create_text(
            300, 200,
            text="You missed!",
            font=('Comic Sans', 50),
            fill='red'
        )
        canvas.after(1000, lambda: canvas.delete(text))
        damage(enemy_hp)

def damage(enemy_hp):
    enemy_hp -= damage
    print("Enemy HP:", enemy_hp)
# ----- Buttons -----
attack_button = tk.Button(canvas, text="Attack", font=("Arial", 18), command=attack)
canvas.create_window(300, 350, window=attack_button)

skill_button = tk.Button(canvas, text="Skill", font=("Arial", 18), command=skill)
canvas.create_window(400, 350, window=skill_button)

root.mainloop()