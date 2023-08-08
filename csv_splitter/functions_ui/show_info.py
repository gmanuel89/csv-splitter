## Import libraries
import os, platform

## Show repository info
def show_info(redirect_url: str):
    # Retrieve the system
    system_os = platform.system()
    if system_os == "Linux":
        os.system("xdg-open " + redirect_url)
    elif system_os == "Darwin":
        os.system("open " + redirect_url)
    elif system_os == "Windows":
        os.system("cmd /c start " + redirect_url)