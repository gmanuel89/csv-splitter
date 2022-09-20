## Import libraries and functions
from functions_ui.csv_file_splitter_button_function import *
import tkinter
from tkinter import font

def get_csv_file_splitter_button(window: tkinter.Tk, text_to_display: str, number_of_output_chunks_entry: tkinter.Entry, ui_fonts: dict[str,font.Font], input_file: str, input_file_name: str, output_folder: str):
    csv_file_splitter_button = tkinter.Button(window, text=text_to_display, command=lambda: csv_file_splitter_button_function(number_of_output_chunks_entry, input_file, input_file_name, output_folder), background = "white", font=ui_fonts.get('button_font'))
    csv_file_splitter_button.grid(row=4, column=0, padx = 2, pady = 2)