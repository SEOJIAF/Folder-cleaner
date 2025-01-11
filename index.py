import os
import shutil

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


dowland_path = os.path.join(os.path.expanduser("~"), "Downloads")



# images
destination_img = os.path.join(os.path.expanduser("~"), r"Documents\stuff\images")
# videos
destination_vid = os.path.join(os.path.expanduser("~"), r"Documents\stuff\videos")



for file in os.listdir(dowland_path):
    if file.endswith((".png", ".jpeg", ".jpg", ".webp", ".gif")):
        
        try:
            print("")
            print(f"Moving {file}")
            source_path = os.path.join(dowland_path, file)
            destination_path = os.path.join(destination_img, file)
            shutil.move(source_path, destination_path)
            print(bcolors.OKGREEN + "moving succesfull"  + bcolors.ENDC)

        except Exception as e:
            print(f'\033[31m\033[44mError moving file {file}: {e}\033[0m')


    elif file.endswith((".mp4", ".MOV", ".AVI", ".webm")):
        try:
            print("")
            print(f"Moving {file}")
            source_path = os.path.join(dowland_path, file)
            destination_path = os.path.join(destination_vid, file)
            shutil.move(source_path, destination_path)
            print(bcolors.OKGREEN + "moving succesfull"  + bcolors.ENDC)
        except Exception as e:
            print(f"Error moving file {file}: {e}")
            

    else:
        print(bcolors.WARNING + f"not a place to sort {file}" + bcolors.ENDC)