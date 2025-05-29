import customtkinter as ctk
from CTkColorPicker import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def color_picker():
    ask_color = AskColor(title="Choose a color")
    hex_color = ask_color.get().lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) # convert hex to rgb

    if rgb:
        return rgb  
    return None

