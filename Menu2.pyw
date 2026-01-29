import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def main():
    root = tk.Tk()
    root.title("Menu")
    root.geometry("600x400")
    root.resizable(False, False)

    # canvas for background and title
    canvas = tk.Canvas(root, width=600, height=400, bg="pink")
    canvas.pack()
    root.update()  # forces geometry update
    print(f"Window width: {root.winfo_width()}")
    print(f"Canvas width: {canvas.winfo_width()}")

    canvas.create_text(300, 150, text="Game", font=("Arial", 40, "bold"), fill="black")

    folder = os.path.dirname(os.path.abspath(sys.argv[0]))
    game_path = os.path.join(folder, "openworld3.py")

    def start_game():
        if not os.path.isfile(game_path):
            messagebox.showerror("Error", f"Cannot find game:\n{game_path}")
            return
        try:
            subprocess.Popen([sys.executable, game_path], close_fds=True)
            root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start game:\n{e}")

    def exit_game():
        root.destroy()

    start_button = tk.Button(root, text="Start", font=("Arial", 18, "bold"),fg="white", bg="green", activebackground="darkgreen", activeforeground="white", command=start_game)
    start_button.place(x=250, y=300, width=100, height=50)

    exit_button = tk.Button(root, text="X", font=("Arial", 18, "bold"), fg="white", bg="red", activebackground="darkred", activeforeground="white", bd=0, command=exit_game)
    def place_exit_button():
        window_width = root.winfo_width()
        button_width = 20
        margin = 20
        x_pos = window_width - button_width - margin
        exit_button.place(x=x_pos, y=margin, width=button_width, height=button_width)

    root.after(100, place_exit_button)

    root.mainloop()

if __name__ == "__main__":
    main()
