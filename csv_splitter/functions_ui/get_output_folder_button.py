## Import libraries and functions
import tkinter
from tkinter import font
from functions_ui.select_output_folder_button_function import select_output_folder_button_function

## Get output folder button
def get_output_folder_button(window: tkinter.Tk, text_to_display: str, ui_fonts: dict[str,font.Font], ui_coordinates: tuple) -> tkinter.Button:
    select_output_folder_button = tkinter.Button(window, text=text_to_display, command=lambda: select_output_folder_button_function(window, ui_fonts), background = "white", font=ui_fonts.get('button_font'))
    select_output_folder_button.grid(row=ui_coordinates[0], column=ui_coordinates[1], padx = 2, pady = 2)
    return select_output_folder_button