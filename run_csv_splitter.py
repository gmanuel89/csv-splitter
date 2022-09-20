## Import functions
from functions_ui.select_input_csv_file import *
from functions_ui.select_output_folder import *
from functions_ui.show_info import *
from functions_ui.close_program import *
from functions_ui.get_ui_fonts import *
from functions_ui.get_csv_file_splitter_button import *
from functions_ui.get_number_of_output_chunks_from_entry import *
from functions_ui.get_title_label import *
from functions.split_csv_file_into_chunks import *
from functions_ui.get_number_of_chunks_label import *
from functions_ui.get_number_of_chunks_entry import *
from functions_ui.get_quit_button import *
from functions_ui.get_output_folder_button import *
from functions_ui.get_csv_file_selection_button import *


from constants import *

## Import libraries
import os, tkinter

# Initialise variables
output_folder = os.getcwd()
input_file = ''
input_file_name = ''

## WINDOW
### Main window
window = tkinter.Tk()
window.title("CSV splitter")
window.resizable(False, False)
window.configure(background = "white")
#window.wm_minsize(width=550, height=600)

# Get the resolution of the screen (to adjust the font size accordingly)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get UI fonts
ui_fonts = get_ui_fonts(window)
#print(ui_fonts)


## UI elements
# Title / Info
get_title_label(window, title_label, github_wiki_url, ui_fonts)
# Number of chunks
get_number_of_chunks_label(window, number_of_chunks_label, ui_fonts)
number_of_output_chunks_entry = get_number_of_chunks_entry(window, ui_fonts, number_of_chunks_entry_default_value)
# Quit
get_quit_button(window, quit_button_label, ui_fonts)
# Output folder
get_output_folder_button(window, output_folder_button_label, ui_fonts, output_folder)
get_output_folder_label(window, output_folder, ui_fonts)
# Input file selection
get_csv_file_selection_button(window, csv_file_selection_button_label, ui_fonts, input_file)
get_csv_file_selection_label(window, input_file, ui_fonts)
# CSV split
get_csv_file_splitter_button(window, csv_file_splitter_button_label, number_of_output_chunks_entry, ui_fonts, input_file, input_file_name, output_folder)


## Hold until quit
window.mainloop()





