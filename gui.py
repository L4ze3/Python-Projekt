import tkinter as tk
from tkinter import colorchooser

def color_picker():
    root = tk.Tk()
    root.withdraw()

    color_code = colorchooser.askcolor(title="Choose a color")
    root.destroy()

    if color_code and color_code[1]:
        return color_code  
    return None