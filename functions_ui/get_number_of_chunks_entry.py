## Import libraries and functions
import tkinter
from tkinter import font

## Number of chunks entry
def get_number_of_chunks_entry(window, ui_fonts: dict[str,font.Font], default_value: str, ui_coordinates: tuple) -> tkinter.Entry:
    number_of_output_chunks_entry = tkinter.Entry(window, justify="center", width=10, font=ui_fonts.get('entry_font'))
    number_of_output_chunks_entry.insert(0, default_value)
    number_of_output_chunks_entry.grid(row=ui_coordinates[0], column=ui_coordinates[1], padx = 2, pady = 2)
    return number_of_output_chunks_entry