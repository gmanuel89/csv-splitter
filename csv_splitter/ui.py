## Import libraries and functions
from csv_splitter.libraries import *
from csv_splitter.constants import *
from csv_splitter.functions import *
from csv_splitter.functions_ui import *

## WINDOW
### Main window
window = Tk()
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
get_output_folder_button(window, output_folder_button_label, ui_fonts)
get_output_folder_label(window, output_folder, ui_fonts)
# Input file selection
get_csv_file_selection_button(window, csv_file_selection_button_label, ui_fonts)
get_csv_file_selection_label(window, input_file, ui_fonts)
# CSV split
get_csv_file_splitter_button(window, csv_file_splitter_button_label, number_of_output_chunks_entry, ui_fonts)


## Hold until quit
mainloop()





