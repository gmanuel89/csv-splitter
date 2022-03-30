## Import libraries
from csv_splitter.libraries import *

# Initialise variables
output_folder = os.getcwd()
input_file = ""


## Define the input CSV file
def select_input_csv_file():
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


## Define where to save the CSV files
def select_output_folder():
    global output_folder
    """
    Tk().withdraw()
    messagebox.showinfo(title='Folder selection', message='Select where to save the CSV files originating from the split')
    """
    # Where to save the GCODE file (escape function environment)
    global output_folder
    Tk().withdraw()
    output_folder = filedialog.askdirectory ()
    # Fix the possible non-defined output folder
    if output_folder == '':
        output_folder = os.getcwd()
    # Just to confirm...
    Tk().withdraw()
    messagebox.showinfo(title='Folder selected', message="The CSV file(s) will be saved in '%s'" %(output_folder))
    return output_folder


## Show repository info
def show_info(github_wiki_url):
    # Retrieve the system
    system_os = platform.system()
    if system_os == "Linux":
        os.system("xdg-open " + github_wiki_url)
    elif system_os == "Darwin":
        os.system("open " + github_wiki_url)
    elif system_os == "Windows":
        os.system("cmd /c start " + github_wiki_url)


## Close program
def close_program(window):
    # Collapse the GUI Tk window
    window.destroy()
    # Quit the Python session
    return quit()


# Get number of output chunks from UI entry
def get_number_of_output_chunks_from_entry(number_of_output_chunks_entry):
    # Get the number of chunks from the entry
    number_of_output_chunks = int(number_of_output_chunks_entry.get())
    if number_of_output_chunks == 0 : number_of_output_chunks = 1
    return number_of_output_chunks

## Function to open the original CSV file and split it
def split_csv_file_into_chunks(number_of_output_chunks):
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
