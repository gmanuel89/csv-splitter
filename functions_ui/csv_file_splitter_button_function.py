## Import libraries and functions
import tkinter
from functions_ui.get_number_of_output_chunks_from_entry import get_number_of_output_chunks_from_entry
from functions.split_csv_file_into_chunks import split_csv_file_into_chunks
import data_lake.global_variables

## CSV file splitter button
def csv_file_splitter_button_function(number_of_output_chunks_entry: tkinter.Entry):
    number_of_output_chunks = get_number_of_output_chunks_from_entry(number_of_output_chunks_entry)
    data_lake.global_variables.number_of_output_chunks = number_of_output_chunks
    input_file = data_lake.global_variables.input_file
    input_file_name = data_lake.global_variables.input_file_name
    output_folder = data_lake.global_variables.output_folder
    split_csv_file_into_chunks(input_file, input_file_name, number_of_output_chunks, output_folder)