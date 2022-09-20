## Import libraries and functions
import tkinter
from tkinter import font
from functions_ui.select_output_folder import *
from functions_ui.refresh_output_folder_label import *

## Output folder button
def select_output_folder_button_function(window: tkinter.Tk, output_folder: str, ui_fonts: dict[str,font.Font]):
    output_folder = select_output_folder()
    refresh_output_folder_label(window, output_folder, ui_fonts)