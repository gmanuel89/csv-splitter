## Import libraries
import tkinter

## Close program
def close_program(window: tkinter.Tk):
    # Collapse the GUI Tk window
    window.destroy()
    # Quit the Python session
    return quit()