## Import libraries and functions
from functions_ui.csv_file_splitter_button_function import csv_file_splitter_button_function
import tkinter
from tkinter import font

def get_csv_file_splitter_button(window: tkinter.Tk, text_to_display: str, number_of_output_chunks_entry: tkinter.Entry, ui_fonts: dict[str,font.Font]) -> tkinter.Button:
    csv_file_splitter_button = tkinter.Button(window, text=text_to_display, command=lambda: csv_file_splitter_button_function(number_of_output_chunks_entry), background = "white", font=ui_fonts.get('button_font'))
    csv_file_splitter_button.grid(row=4, column=0, padx = 2, pady = 2)
    return csv_file_splitter_button