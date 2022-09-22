## Import libraries
import csv, os, math
from tkinter import Tk, messagebox

## Function to open the original CSV file and split it
def split_csv_file_into_chunks(input_file: str, input_file_name: str, number_of_output_chunks: int, output_folder: str):
    print('NUMBER OF CHUNKS: ' + str(number_of_output_chunks))
    print('INPUT FILE: ' + input_file)
    print('INPUT FILE NAME: ' + input_file_name)
    print('OUTPUT FOLDER: ' + output_folder)
    # Open the CSV file and split it into chunks
    with open (input_file, 'r', encoding='UTF8') as input_csv_file:
        input_csv_file_lines = list(csv.reader(input_csv_file))
        # Store the header (to be placed at every csv)
        csv_header = input_csv_file_lines[0]
        # The actual lines are beyond the header
        number_of_lines = len(input_csv_file_lines) - 1
        print ('number of lines: ', number_of_lines)
        number_of_lines_per_chunk = math.ceil(number_of_lines / number_of_output_chunks)
        print ('number of lines per chunk: ', number_of_lines_per_chunk)
        # Initialise index variables
        lower_index = None
        higher_index = None
        # Start cycling after the header
        for i in range(number_of_output_chunks):
            if lower_index is None : lower_index = 1
            else : lower_index = lower_index + number_of_lines_per_chunk
            if higher_index is None : higher_index = number_of_lines_per_chunk + 1
            else: higher_index = higher_index + number_of_lines_per_chunk
            # Do not go over the length of the file lines
            if higher_index >= number_of_lines + 1 : higher_index = number_of_lines + 1
            # Retrieve the lines to be put into the output
            output_lines = input_csv_file_lines[lower_index:higher_index]
            print('Number of lines in iteration n.' + str(i+1) + ': ', str(len(output_lines)))
            # Break out if there are no more lines
            if len(output_lines) == 0: break
            # Output file name
            output_file_name = '(' + str(i+1) + ')' + ' ' + input_file_name
            # Go to the output folder and save the files
            os.chdir(output_folder)
            with open (output_file_name, 'w', encoding='UTF8', newline='') as output_file:
                csv_writer = csv.writer(output_file)
                csv_writer.writerow(csv_header)
                for line in output_lines:
                    csv_writer.writerow(line)
                output_file.close()
        input_csv_file.close()
        # Success
        Tk().withdraw()
        messagebox.showinfo(title='Success!', message='The input CSV has been successfully split into %s chunks!' %(number_of_output_chunks))
