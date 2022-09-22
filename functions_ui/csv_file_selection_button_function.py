## Import libraries and functions
import tkinter
from tkinter import font
from functions_ui.select_input_csv_file import select_input_csv_file
from functions_ui.refresh_csv_file_selection_label import refresh_csv_file_selection_label
import data_lake.global_variables

## CSV selection button
def csv_file_selection_button_function(window: tkinter.Tk, ui_fonts: dict[str,font.Font]) -> str:
    input_file, input_file_name = select_input_csv_file()
    refresh_csv_file_selection_label(window, input_file, ui_fonts)
    data_lake.global_variables.input_file = input_file
    data_lake.global_variables.input_file_name = input_file_name
    return input_file