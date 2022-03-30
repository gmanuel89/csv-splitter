
from libraries import *
from functions import *

def get_output_folder_label(window, output_folder, font):
    global output_folder_label
    output_folder_label = Label(window, text=output_folder, background="white", width=30, font=font)
    output_folder_label.grid(row=3, column=1, padx = 2, pady = 2)
    return output_folder_label


def get_output_folder_button(window, font):
    global select_output_folder_button
    select_output_folder_button = Button(window, text='Select output folder...', command=select_output_folder, background = "white", font=font)
    select_output_folder_button.grid(row=3, column=0, padx = 2, pady = 2)
    return select_output_folder_button


def get_number_of_chunks_label(window, font):
    global number_of_output_chunks_label
    number_of_output_chunks_label = Label(window, text="Insert number of chunks", background="white", width=30, font=font)
    number_of_output_chunks_label.grid(row=1, column=0, padx = 2, pady = 2)
    return number_of_output_chunks_label

def get_number_of_chunks_entry(window, font, default_value):
    global number_of_output_chunks_entry
    number_of_output_chunks_entry = Entry(window, justify="center", width=10, font=font)
    number_of_output_chunks_entry.insert(0, default_value)
    number_of_output_chunks_entry.grid(row=1, column=1, padx = 2, pady = 2)
    return number_of_output_chunks_entry