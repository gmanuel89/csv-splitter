## Import libraries and functions
from csv_splitter.libraries import *
from csv_splitter.functions import *


# Title label
def get_title_label(window, title_label, link_for_redirect, ui_fonts):
    title_label = Button(window, text=title_label, relief="flat", background="white", font=ui_fonts.get('title_font'), command=lambda: show_info(link_for_redirect))
    title_label.grid(row=0, column=0, columnspan = 2, padx = 20, pady = 20)


# Output folder label
def get_output_folder_label(window, output_folder, ui_fonts):
    global output_folder_label
    output_folder_label = Label(window, text=output_folder, background="white", width=30, font=ui_fonts.get('label_font'))
    output_folder_label.grid(row=3, column=1, padx = 2, pady = 2)
    return output_folder_label

def refresh_output_folder_label(window, output_folder, ui_fonts):
    return get_output_folder_label(window, output_folder, ui_fonts)


# Output folder button
def select_output_folder_button_function(window, output_folder, ui_fonts):
    output_folder = select_output_folder()
    refresh_output_folder_label(window, output_folder, ui_fonts)

def get_output_folder_button(window, text_to_display, ui_fonts):
    global select_output_folder_button
    select_output_folder_button = Button(window, text=text_to_display, command=lambda: select_output_folder_button_function(window, output_folder, ui_fonts), background = "white", font=ui_fonts.get('button_font'))
    select_output_folder_button.grid(row=3, column=0, padx = 2, pady = 2)
    return select_output_folder_button


# Number of chunks label
def get_number_of_chunks_label(window, text_to_display, ui_fonts):
    global number_of_output_chunks_label
    number_of_output_chunks_label = Label(window, text=text_to_display, background="white", width=30, font=ui_fonts.get('label_font'))
    number_of_output_chunks_label.grid(row=1, column=0, padx = 2, pady = 2)
    return number_of_output_chunks_label


# Number of chunks entry
def get_number_of_chunks_entry(window, ui_fonts, default_value):
    global number_of_output_chunks_entry
    number_of_output_chunks_entry = Entry(window, justify="center", width=10, font=ui_fonts.get('entry_font'))
    number_of_output_chunks_entry.insert(0, default_value)
    number_of_output_chunks_entry.grid(row=1, column=1, padx = 2, pady = 2)
    return number_of_output_chunks_entry


# CSV selection label
def get_csv_file_selection_label(window, input_file, ui_fonts):
    global csv_file_selection_label
    csv_file_selection_label = Label(window, text=input_file, background="white", width=30, font=ui_fonts.get('label_font'))
    csv_file_selection_label.grid(row=2, column=1, padx = 2, pady = 2)
    return csv_file_selection_label

def refresh_csv_file_selection_label(window, input_file, ui_fonts):
    return get_csv_file_selection_label(window, input_file, ui_fonts)


# CSV selection button
def csv_file_selection_button_function(window, input_file, ui_fonts):
    input_file = select_input_csv_file()
    refresh_csv_file_selection_label(window, input_file, ui_fonts)

def get_csv_file_selection_button(window, text_to_display, ui_fonts):
    csv_file_selection_button = Button(window, text=text_to_display, command=lambda: csv_file_selection_button_function(window, input_file, ui_fonts), background = "white", font=ui_fonts.get('button_font'))
    csv_file_selection_button.grid(row=2, column=0, padx = 2, pady = 2)
    return csv_file_selection_button


# Quit button
def get_quit_button(window, text_to_display, ui_fonts):
    quit_button = Button(window, text=text_to_display, command=lambda: close_program(window), background="white", font=ui_fonts.get('button_font'))
    quit_button.grid(row=5, column=0, columnspan = 2, padx = 2, pady = 2)


# CSV file splitter button
def csv_file_splitter_button_function(number_of_output_chunks_entry):
    number_of_output_chunks = get_number_of_output_chunks_from_entry(number_of_output_chunks_entry)
    split_csv_file_into_chunks(number_of_output_chunks)

def get_csv_file_splitter_button(window, text_to_display, number_of_output_chunks_entry, ui_fonts):
    csv_file_splitter_button = Button(window, text=text_to_display, command=lambda: csv_file_splitter_button_function(number_of_output_chunks_entry), background = "white", font=ui_fonts.get('button_font'))
    csv_file_splitter_button.grid(row=4, column=0, padx = 2, pady = 2)


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
            # Use them in the GUI
            title_font = ubuntu_title_bold
            label_font = ubuntu_other_normal
            entry_font = ubuntu_other_normal
            button_font = ubuntu_other_bold
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