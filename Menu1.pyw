import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def main():
    root = tk.Tk()
    root.title("Menu")
    canvas = tk.Canvas(root, width=600, height=400, bg="pink")
    canvas.pack()
    canvas.create_text(300, 200, text="Game", font=("Arial", 40), fill="black")

    # Absolute path to the game
    folder = os.path.dirname(os.path.abspath(sys.argv[0]))
    game_path = os.path.join(folder, "openworld3.py")

    # Button callbacks
    def start():
        print("game started")
        if not os.path.isfile(game_path):
            messagebox.showerror("Error", f"Cannot find game:\n{game_path}")
            return
        try:
            subprocess.Popen([sys.executable, game_path], shell=True)
            root.destroy()  # close menu
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start game:\n{e}")

    def exit_game():
        print("game exited")
        root.destroy()

    # Buttons
    start_button = tk.Button(canvas, text="Start", font=("Arial", 18), command=start)
    canvas.create_window(300, 350, window=start_button)

    exit_button = tk.Button(canvas, text="Exit", font=("Arial", 18), command=exit_game)
    canvas.create_window(550, 50, window=exit_button)

    root.mainloop()

if __name__ == "__main__":
    main()
