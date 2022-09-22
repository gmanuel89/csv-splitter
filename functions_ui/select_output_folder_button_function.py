## Import libraries and functions
import tkinter
from tkinter import font
from functions_ui.select_output_folder import select_output_folder
from functions_ui.refresh_output_folder_label import refresh_output_folder_label
import data_lake.global_variables

## Output folder button
def select_output_folder_button_function(window: tkinter.Tk, ui_fonts: dict[str,font.Font]) -> str:
    output_folder = select_output_folder()
    refresh_output_folder_label(window, output_folder, ui_fonts)
    data_lake.global_variables.output_folder = output_folder
    return output_folder