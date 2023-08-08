## Initialisation
from data_lake.constants import *
import data_lake.global_variables
from data_lake.ui_constants import *

## Import functions
from functions_ui import *

## Import libraries
import tkinter

## Initialise variables
output_folder = data_lake.global_variables.output_folder
input_file = data_lake.global_variables.input_file
input_file_name = data_lake.global_variables.input_file_name
number_of_output_chunks = data_lake.global_variables.number_of_output_chunks

## WINDOW
### Main window
window = tkinter.Tk()
window.title("CSV splitter")
window.resizable(False, False)
window.configure(background = "white")
#window.wm_minsize(width=550, height=600)

# Get UI fonts
ui_fonts = get_ui_fonts(window)
#print(ui_fonts)

## UI elements
# Title / Info
get_title_label(window, TITLE_LABEL, GITHUB_WIKI_URL, ui_fonts, TITLE_LABEL_COORDINATES)
# Number of chunks
get_number_of_chunks_label(window, NUMBER_OF_CHUNKS_LABEL, ui_fonts, NUMBER_OF_CHUNKS_LABEL_COORDINATES)
number_of_output_chunks_entry = get_number_of_chunks_entry(window, ui_fonts, NUMBER_OF_CHUNKS_ENTRY_DEFAULT_VALUE, NUMBER_OF_CHUNKS_ENTRY_COORDINATES)
# Quit
get_quit_button(window, QUIT_BUTTON_LABEL, ui_fonts, QUIT_BUTTON_COORDINATES)
# Output folder
get_output_folder_button(window, OUTPUT_FOLDER_BUTTON_LABEL, ui_fonts, OUTPUT_FOLDER_BUTTON_COORDINATES)
get_output_folder_label(window, output_folder, ui_fonts, OUTPUT_FOLDER_LABEL_COORDINATES)
# Input file selection
get_csv_file_selection_button(window, CSV_FILE_SELECTION_BUTTON_LABEL, ui_fonts, CSV_FILE_SELECTION_BUTTON_COORDINATES)
get_csv_file_selection_label(window, input_file, ui_fonts, CSV_FILE_SELECTION_LABEL_COORDINATES)
# CSV split
get_csv_file_splitter_button(window, CSV_FILE_SPLITTER_BUTTON_LABEL, number_of_output_chunks_entry, ui_fonts, CSV_FILE_SPLITTER_BUTTON_COORDINATES)

## Hold until quit
window.mainloop()
