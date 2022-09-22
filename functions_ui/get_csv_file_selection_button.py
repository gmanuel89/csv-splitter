## Import libraries and functions
import tkinter
from tkinter import font
from functions_ui.csv_file_selection_button_function import csv_file_selection_button_function

## CSV file selection button
def get_csv_file_selection_button(window: tkinter.Tk, text_to_display: str, ui_fonts: dict[str,font.Font]) -> tkinter.Button:
    csv_file_selection_button = tkinter.Button(window, text=text_to_display, command=lambda: csv_file_selection_button_function(window, ui_fonts), background = "white", font=ui_fonts.get('button_font'))
    csv_file_selection_button.grid(row=2, column=0, padx = 2, pady = 2)
    return csv_file_selection_button