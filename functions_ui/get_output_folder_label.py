## Import libraries and functions
import tkinter
from tkinter import font

## Output folder label
def get_output_folder_label(window: tkinter.Tk, output_folder: str, ui_fonts: dict[str,font.Font]) -> tkinter.Label:
    output_folder_label = tkinter.Label(window, text=output_folder, background="white", width=100, font=ui_fonts.get('label_font'))
    output_folder_label.grid(row=3, column=1, padx = 2, pady = 2)
    return output_folder_label