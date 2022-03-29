# Import libraries
import csv, os, math
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from tkinter import Entry, messagebox, filedialog

# Before we start
tkinter.Tk().withdraw()
messagebox.showinfo(title='CSV splitter', message='This application will split a CSV file in chunks')

# Message for selection (open)
tkinter.Tk().withdraw()
messagebox.showinfo(title='CSV selection', message='Select the CSV file to be split in chunks')

#  Input CSV selection
tkinter.Tk().withdraw()
input_file = filedialog.askopenfilename(filetypes=[('CSV files','.csv')])
# Get the file name
input_file_name_split = input_file.split('/')
input_file_name = input_file_name_split[len(input_file_name_split)-1]

# Message for selection (save)
tkinter.Tk().withdraw()
tkinter.messagebox.showinfo(title='Folder selection', message='Select where to save the CSV files originating from the split')

# Where to save the CSV files
tkinter.Tk().withdraw()
output_folder = filedialog.askdirectory(title='CSV folder selection')
os.chdir(output_folder)

# Number of chunks
number_of_output_chunks = 2
"""
window = tkinter.Tk()
e = Entry(window)
"""
if number_of_output_chunks == 0 : number_of_output_chunks = 1

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
        with open (output_file_name, 'w', encoding='UTF8', newline='') as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerow(csv_header)
            for line in output_lines:
                csv_writer.writerow(line)
            output_file.close()
    input_csv_file.close()

"""
with open (output_file, 'w', encoding='UTF8', newline='') as outputfile:
    csv_writer = csv.writer(outputfile)
    headers = ['Image', 'Binary']
    #print('Writing headers: ', headers)
    csv_writer.writerow(headers)        
    for i in range(len(list_of_files)):
        with open(list_of_files[i], "rb") as image_file:
            print ('Opening the file: ', list_of_files[i])
            image_file_b64_encoded = base64.b64encode(image_file.read())
        image_file.close()
        csv_row = [str(list_of_files[i]), str(image_file_b64_encoded)]
        #print('Writing row: ', csv_row)
        csv_writer.writerow(csv_row)
"""

# Success
tkinter.Tk().withdraw()
tkinter.messagebox.showinfo(title='Success!', message='The input CSV has been successfully split into chunks!')
