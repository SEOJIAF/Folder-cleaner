# File Sorter Script

A Python script to organize files in your `Downloads` folder by moving them to designated folders for images and videos. Any unsupported file types will remain in the `Downloads` folder with a warning message.

---

## Features

- **Automatic Sorting**: 
  - Moves image files (`.png`, `.jpeg`, `.jpg`, `.webp`, `.gif`) to the `Documents/stuff/images` folder.
  - Moves video files (`.mp4`, `.MOV`, `.AVI`, `.webm`) to the `Documents/stuff/videos` folder.
- **Custom Console Outputs**: 
  - Color-coded messages for success, warnings, and errors using ANSI escape sequences.
- **Error Handling**: 
  - Provides error messages if a file cannot be moved.

---

## How It Works

1. **Scan the `Downloads` Folder**: The script iterates through all files in the `Downloads` directory.
2. **Classify Files**:
   - **Images**: Files with extensions `.png`, `.jpeg`, `.jpg`, `.webp`, `.gif`.
   - **Videos**: Files with extensions `.mp4`, `.MOV`, `.AVI`, `.webm`.
3. **Move Files**: Files are moved to pre-defined directories (`Documents/stuff/images` or `Documents/stuff/videos`).
4. **Handle Unsupported Files**: Files with unsupported extensions are skipped, and a warning is displayed.

---

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/SEOJIAF/Folder-cleaner

---
## Usage

    Open your terminal or command prompt.
    Run the script:

    python file_sorter.py

    The script will organize files in your Downloads folder.
---
## Configuration

The script uses the following default paths:

    Source: Downloads folder in the user's home directory.
    Destinations:
        Images: Documents/stuff/images
        Videos: Documents/stuff/videos

You can modify these paths in the script:

dowland_path = os.path.join(os.path.expanduser("~"), "Downloads")
destination_img = os.path.join(os.path.expanduser("~"), r"Documents\stuff\images")
destination_vid = os.path.join(os.path.expanduser("~"), r"Documents\stuff\videos")



This script uses built-in Python libraries:

    os
    shutil

No external libraries are required.
