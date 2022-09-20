## Import libraries
from tkinter import Tk, filedialog, messagebox

## Define the input CSV file
def select_input_csv_file() -> str:
    global input_file, input_file_name
    Tk().withdraw()
    input_file = filedialog.askopenfilename(filetypes=[('CSV files','.csv')])
    # Get the file name
    input_file_name_split = input_file.split('/')
    input_file_name = input_file_name_split[len(input_file_name_split)-1]
    # Just to confirm...
    Tk().withdraw()
    messagebox.showinfo(title='CSV file selected', message="The CSV file selected is '%s'" %(input_file))
    return input_file