## Import libraries and functions
import tkinter
from tkinter import font
from functions_ui.select_input_csv_file import *
from functions_ui.refresh_csv_file_selection_label import *

## CSV selection button
def csv_file_selection_button_function(window: tkinter.Tk, input_file: str, ui_fonts: dict[str,font.Font]):
    input_file = select_input_csv_file()
    refresh_csv_file_selection_label(window, input_file, ui_fonts)