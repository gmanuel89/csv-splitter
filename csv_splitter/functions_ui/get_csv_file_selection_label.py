## Import libraries and functions
import tkinter
from tkinter import font

## CSV selection label
def get_csv_file_selection_label(window: tkinter.Tk, input_file: str, ui_fonts: dict[str,font.Font], ui_coordinates: tuple) -> tkinter.Label:
    global csv_file_selection_label
    csv_file_selection_label = tkinter.Label(window, text=input_file, background="white", width=100, font=ui_fonts.get('label_font'))
    csv_file_selection_label.grid(row=ui_coordinates[0], column=ui_coordinates[1], padx = 2, pady = 2)
    return csv_file_selection_label