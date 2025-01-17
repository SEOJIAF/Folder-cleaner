import os
import shutil
import ctypes
from send2trash import send2trash  # Use send2trash for Recycle Bin functionality

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


download_path = os.path.join(os.path.expanduser("~"), "Downloads")
# Destination paths
destination_img = os.path.join(os.path.expanduser("~"), "Documents", "stuff", "images")
destination_vid = os.path.join(os.path.expanduser("~"), "Documents", "stuff", "videos")
destination_doc = os.path.join(os.path.expanduser("~"), "Documents", "stuff", "docx")

# Create destination directories if they do not exist
os.makedirs(destination_img, exist_ok=True)
os.makedirs(destination_vid, exist_ok=True)
os.makedirs(destination_doc, exist_ok=True)

# Function to move files
def presunSubory(file, destination):
    try:
        print("")
        print(f"Moving {file}")
        source_path = os.path.join(download_path, file)
        destination_path = os.path.join(destination, file)
        shutil.move(source_path, destination_path)
        print(bcolors.OKGREEN + f"Moved '{file}' successfully" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + f"Error moving file '{file}': {e}" + bcolors.ENDC)

# Function to send files to the Recycle Bin
def send_to_bin(file):
    try:
        source_path = os.path.join(download_path, file)
        send2trash(source_path)
        print("")
        print(bcolors.WARNING + f"Sent '{file}' to Recycle Bin" + bcolors.ENDC)
    except Exception as e:
        print("")
        print(bcolors.FAIL + f"Error sending '{file}' to Recycle Bin: {e}" + bcolors.ENDC)

# Function to empty the Recycle Bin
def empty_recycle_bin():
    try:
        result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x1 | 0x2 | 0x4)
        if result == 0:
            print(bcolors.OKGREEN + "Recycle Bin successfully emptied." + bcolors.ENDC)
        else:
            print(bcolors.FAIL + f"Failed to empty Recycle Bin. It's empty" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + f"Error while emptying Recycle Bin: {e}" + bcolors.ENDC)

# Main logic
for file in os.listdir(download_path):
    if file.endswith((".png", ".jpeg", ".jpg", ".webp", ".gif", "ico")):
        presunSubory(file, destination_img)
    elif file.endswith((".mp4", ".MOV", ".AVI", ".webm")):
        presunSubory(file, destination_vid)
    elif file.endswith((".docx", ".doc", ".odt", ".txt", ".rtf", "pages", ".gdoc")):
        presunSubory(file, destination_doc)
    else:
        send_to_bin(file)

print("")
print(bcolors.OKGREEN + f"{download_path} is clean" + bcolors.ENDC)

# Ask the user if they want to clear the Recycle Bin
bin_clear = input("Do you want to clear the Recycle Bin too? (y/n): ").strip().lower()

if bin_clear == "y":
    empty_recycle_bin()
else:
    print("Cleaning process complete.")
