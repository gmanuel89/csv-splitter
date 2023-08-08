## Import libraries and functions
import tkinter
from tkinter import font
from functions_ui.close_program import close_program

## Quit button
def get_quit_button(window: tkinter.Tk, text_to_display: str, ui_fonts: dict[str,font.Font], ui_coordinates: tuple) -> tkinter.Button:
    quit_button = tkinter.Button(window, text=text_to_display, command=lambda: close_program(window), background="white", font=ui_fonts.get('button_font'))
    quit_button.grid(row=ui_coordinates[0], column=ui_coordinates[1], columnspan = 2, padx = 2, pady = 2)
    return quit_button