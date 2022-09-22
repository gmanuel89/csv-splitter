## Import libraries
import tkinter

## Get number of output chunks from UI entry
def get_number_of_output_chunks_from_entry(number_of_output_chunks_entry: tkinter.Entry) -> int:
    global number_of_output_chunks
    # Get the number of chunks from the entry
    number_of_output_chunks = int(number_of_output_chunks_entry.get())
    if number_of_output_chunks == 0 : number_of_output_chunks = 1
    return number_of_output_chunks