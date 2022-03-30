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
print(ui_fonts)


## UI elements
# Title / Info
title_label = Button(window, text="CSV file splitter", relief="flat", background="white", font=ui_fonts.get('title_font'), command=lambda: show_info(github_wiki_url))
# Number of chunks
get_number_of_chunks_label(window, ui_fonts.get('label_font'))
number_of_output_chunks_entry = get_number_of_chunks_entry(window, ui_fonts.get('entry_font'), '2')
# Quit
quit_button = Button(window, text='QUIT', command=lambda: close_program(window), background="white", font=ui_fonts.get('button_font'))
# Output folder
get_output_folder_button(window, ui_fonts.get('button_font'))
get_output_folder_label(window, output_folder, ui_fonts.get('label_font'))
# Input file selection
csv_file_selection_button = Button(window, text='Select input CSV file...', command=select_input_csv_file, background = "white", font=ui_fonts.get('button_font'))
# CSV split
csv_file_splitter_button = Button(window, text='Split CSV file...', command=lambda: split_csv_file_into_chunks(get_number_of_output_chunks_from_entry(number_of_output_chunks_entry)), background = "white", font=ui_fonts.get('button_font'))

## UI elements grid
title_label.grid(row=0, column=0, columnspan = 2, padx = 20, pady = 20)
csv_file_selection_button.grid(row=2, column=0, padx = 2, pady = 2)
csv_file_splitter_button.grid(row=4, column=0, padx = 2, pady = 2)
quit_button.grid(row=5, column=0, columnspan = 2, padx = 2, pady = 2)

## Hold until quit
mainloop()





