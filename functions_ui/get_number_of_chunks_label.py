## Import libraries and functions
import tkinter
from tkinter import font

## Number of chunks label
def get_number_of_chunks_label(window: tkinter.Tk, text_to_display: str, ui_fonts: dict[str,font.Font], ui_coordinates: tuple) -> tkinter.Label:
    number_of_output_chunks_label = tkinter.Label(window, text=text_to_display, background="white", width=30, font=ui_fonts.get('label_font'))
    number_of_output_chunks_label.grid(row=ui_coordinates[0], column=ui_coordinates[1], padx = 2, pady = 2)
    return number_of_output_chunks_label