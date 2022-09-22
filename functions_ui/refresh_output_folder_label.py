## Import libraries and functions
import tkinter
from tkinter import font
from functions_ui.get_output_folder_label import get_output_folder_label

## Refresh output folder label
def refresh_output_folder_label(window, output_folder, ui_fonts: dict[str,font.Font]) -> tkinter.Label:
    return get_output_folder_label(window, output_folder, ui_fonts)