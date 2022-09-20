## Import libraries and functions
from functions_ui.get_number_of_output_chunks_from_entry import *
from functions.split_csv_file_into_chunks import *
import tkinter

## CSV file splitter button
def csv_file_splitter_button_function(number_of_output_chunks_entry: tkinter.Entry, input_file: str, input_file_name: str, output_folder: str):
    number_of_output_chunks = get_number_of_output_chunks_from_entry(number_of_output_chunks_entry)
    split_csv_file_into_chunks(input_file, input_file_name, number_of_output_chunks, output_folder)