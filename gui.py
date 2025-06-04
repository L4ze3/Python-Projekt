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

class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Python Projekt")
        self.geometry("400x300")

        selected_option = ctk.StringVar()
        options = (("Radial", "r"),
                   ("Vertical", "v"),
                   ("Horizontal", "h"),
                   ("Alien", "a"))
        
        for option in options:
            self.radio = ctk.CTkRadioButton(self, text=option[0], value=option[1], variable=selected_option)
            self.radio.pack(pady=10)

        self.checkbox = ctk.CTkCheckBox(self, text="Grayscale")
        self.checkbox.pack(pady=10)

        #self.upload_btn = ctk.CTkButton(self, text="Upload", command=self.upload_file)
        #self.upload_btn.pack(pady=10)

        #self.label = ctk.CTkLabel(self, text="No file selected")
        #self.label.pack()