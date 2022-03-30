## Import libraries
from csv_splitter.libraries import *

# Initialise output folder
output_folder = os.getcwd()


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


# Get fonts for UI
def get_ui_fonts(window):
    ### Store the fonts in a variable for faster editing
    # Get system info (Platform - Release - Version (- Linux Distro))
    system_os = platform.system()
    os_release = platform.release()
    os_version = platform.version()
    # Default sizes (determined on a 1680x1050 screen) (in order to make them adjust to the size screen, the screen resolution should be retrieved)
    #title_font_size = 24
    #other_font_size = 11
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Determine the font size according to the resolution
    total_number_of_pixels = screen_width * screen_height
    # Determine the scaling factor (according to a complex formula)
    scaling_factor_title_font = float((0.03611 * total_number_of_pixels) + 9803.1254)
    scaling_factor_other_font = float((0.07757 * total_number_of_pixels) + 23529.8386)
    title_font_size = int(round(total_number_of_pixels / scaling_factor_title_font))
    other_font_size = int(round(total_number_of_pixels / scaling_factor_other_font))
    # Windows
    if system_os == "Windows":
        # Define the fonts
        garamond_title_bold = font.Font(family = "Garamond", size = title_font_size, weight = "bold")
        garamond_other_normal = font.Font(family = "Garamond", size = other_font_size, weight = "normal")
        garamond_other_bold = font.Font(family = "Garamond", size = other_font_size, weight = "bold")
        arial_title_bold = font.Font(family = "Arial", size = title_font_size, weight = "bold")
        arial_other_normal = font.Font(family = "Arial", size = other_font_size, weight = "normal")
        arial_other_bold = font.Font(family = "Arial", size = other_font_size, weight = "bold")
        trebuchet_title_bold = font.Font(family = "Trebuchet MS", size = title_font_size, weight = "bold")
        trebuchet_other_normal = font.Font(family = "Trebuchet MS", size = other_font_size, weight = "normal")
        trebuchet_other_bold = font.Font(family = "Trebuchet MS", size = other_font_size, weight = "bold")
        calibri_title_bold = font.Font(family = "Calibri", size = title_font_size, weight = "bold")
        calibri_other_normal = font.Font(family = "Calibri", size = other_font_size, weight = "normal")
        calibri_other_bold = font.Font(family = "Calibri", size = other_font_size, weight = "bold")
        # Use them in the GUI
        title_font = calibri_title_bold
        label_font = calibri_other_normal
        entry_font = calibri_other_normal
        button_font = calibri_other_bold
    # Linux
    elif system_os == "Linux":
        # Retrieve the linux distribution
        linux_distro = platform.linux_distribution()
        # Ubuntu
        if "Ubuntu" in linux_distro or "Ubuntu" in os_version:
            # Define the fonts
            ubuntu_title_bold = font.Font(family = "Ubuntu", size = title_font_size, weight = "bold")
            ubuntu_other_normal = font.Font(family = "Ubuntu", size = other_font_size, weight = "normal")
            ubuntu_other_bold = font.Font(family = "Ubuntu", size = other_font_size, weight = "bold")
            cantarell_title_bold = font.Font(family = "Cantarell", size = title_font_size, weight = "bold")
            cantarell_other_normal = font.Font(family = "Cantarell", size = other_font_size, weight = "normal")
            cantarell_other_bold = font.Font(family = "Cantarell", size = other_font_size, weight = "bold")
            bitstream_charter_title_bold = font.Font(family = "Bitstream Charter", size = title_font_size, weight = "bold")
            bitstream_charter_other_normal = font.Font(family = "Bitstream Charter", size = other_font_size, weight = "normal")
            bitstream_charter_other_bold = font.Font(family = "Bitstream Charter", size = other_font_size, weight = "bold")
            liberation_title_bold = font.Font(family = "Liberation Sans", size = title_font_size, weight = "bold")
            liberation_other_normal = font.Font(family = "Liberation Sans", size = other_font_size, weight = "normal")
            liberation_other_bold = font.Font(family = "Liberation Sans", size = other_font_size, weight = "bold")
            # Use them in the GUI
            title_font = ubuntu_title_bold
            label_font = ubuntu_other_normal
            entry_font = ubuntu_other_normal
            button_font = ubuntu_other_bold
        # Fedora
        elif "Fedora" in linux_distro or "Fedora" in os_version:
            # Define the fonts
            liberation_title_bold = font.Font(family = "Liberation Sans", size = title_font_size, weight = "bold")
            liberation_other_normal = font.Font(family = "Liberation Sans", size = other_font_size, weight = "normal")
            liberation_other_bold = font.Font(family = "Liberation Sans", size = other_font_size, weight = "bold")
            cantarell_title_bold = font.Font(family = "Cantarell", size = title_font_size, weight = "bold")
            cantarell_other_normal = font.Font(family = "Cantarell", size = other_font_size, weight = "normal")
            cantarell_other_bold = font.Font(family = "Cantarell", size = other_font_size, weight = "bold")
            # Use them in the GUI
            title_font = cantarell_title_bold
            label_font = cantarell_other_normal
            entry_font = cantarell_other_normal
            button_font = cantarell_other_bold
        # Other linux distros
        else:
            # Define the fonts
            liberation_title_bold = font.Font(family = "Liberation Sans", size = title_font_size, weight = "bold")
            liberation_other_normal = font.Font(family = "Liberation Sans", size = other_font_size, weight = "normal")
            liberation_other_bold = font.Font(family = "Liberation Sans", size = other_font_size, weight = "bold")
            # Use them in the GUI
            title_font = liberation_title_bold
            label_font = liberation_other_normal
            entry_font = liberation_other_normal
            button_font = liberation_other_bold
    elif system_os == "Mac":
        # Define the fonts
        helvetica_title_bold = font.Font(family = "Helvetica", size = title_font_size, weight = "bold")
        helvetica_other_normal = font.Font(family = "Helvetica", size = other_font_size, weight = "normal")
        helvetica_other_bold = font.Font(family = "Helvetica", size = other_font_size, weight = "bold")
        # Use them in the GUI
        title_font = helvetica_title_bold
        label_font = helvetica_other_normal
        entry_font = helvetica_other_normal
        button_font = helvetica_other_bold
    else:
        # Define the fonts
        courier_title_bold = font.Font(family = "Courier New", size = title_font_size, weight = "bold")
        courier_other_normal = font.Font(family = "Courier New", size = other_font_size, weight = "normal")
        courier_other_bold = font.Font(family = "Courier New", size = other_font_size, weight = "bold")
        # Use them in the GUI
        title_font = courier_title_bold
        label_font = courier_other_normal
        entry_font = courier_other_normal
        button_font = courier_other_bold
    #font.families(root = window)
    # return
    ui_fonts = {'title_font': title_font, 'label_font':label_font, 'entry_font': entry_font, 'button_font': button_font}
    return ui_fonts