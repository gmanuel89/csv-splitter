## Import libraries and functions
import tkinter
from tkinter import font
from functions_ui.show_info import show_info

## Title label
def get_title_label(window: tkinter.Tk, title_label: str, link_for_redirect: str, ui_fonts: dict[str,font.Font], ui_coordinates: tuple) -> tkinter.Label:
    title_label = tkinter.Button(window, text=title_label, relief="flat", background="white", font=ui_fonts.get('title_font'), command=lambda: show_info(link_for_redirect))
    title_label.grid(row=ui_coordinates[0], column=ui_coordinates[1], columnspan = 2, padx = 20, pady = 20)
    return title_label