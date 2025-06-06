import customtkinter as ctk
from CTkColorPicker import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Python Projekt")
        self.geometry("400x300")

        self.selected_pattern = ctk.StringVar()
        patterns = (("Radial", "r"),
                   ("Vertical", "v"),
                   ("Horizontal", "h"),
                   ("Alien", "a"))
        
        for pattern in patterns:
            self.radio_pattern = ctk.CTkRadioButton(self, text=pattern[0], value=pattern[1], variable=self.selected_pattern)
            self.radio_pattern.pack(pady=20)


        self.selected_option = ctk.StringVar()
        options = (("Grayscale", "g"),
                   ("Invert", "i"))

        for option in options:
            self.radio_option = ctk.CTkRadioButton(self, text=option[0], value=option[1], variable=self.selected_option)
            self.radio_option.pack(pady=20)


        #self.grayscale = ctk.CTkCheckBox(self, text="Grayscale")
        #self.grayscale.pack(pady=10)

        #self.invert = ctk.CTkCheckBox(self, text="Invert")
        #self.invert.pack(pady=20)

        self.colorpicker = CTkColorPicker(self, orientation='horizontal')
        self.colorpicker.pack(pady=70)

        self.button = ctk.CTkButton(self, text="Generate Image", command=self.get_values)
        self.button.pack(pady=80)

    def get_values(self):
        self.destroy
        pattern = self.selected_pattern.get()
        option = self.selected_option.get()
        color = self.colorpicker.get().lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4)) # convert hex to rgb
        self.quit()
        return (pattern, option, rgb)
