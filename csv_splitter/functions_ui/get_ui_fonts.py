## Import libraries
import tkinter, platform
from tkinter import font

## Get fonts for UI
def get_ui_fonts(window: tkinter.Tk) -> dict[str,font.Font]:
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