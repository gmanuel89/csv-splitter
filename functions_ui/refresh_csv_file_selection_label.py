## Import libraries and functions
import tkinter
from tkinter import font
from functions_ui.get_csv_file_selection_label import *

## Refresh CSV selection label
def refresh_csv_file_selection_label(window: tkinter.Tk, input_file: str, ui_fonts: dict[str,font.Font]) -> tkinter.Label:
    return get_csv_file_selection_label(window, input_file, ui_fonts)