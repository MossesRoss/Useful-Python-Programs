import os
import shutil
from tkinter.filedialog import askdirectory

def move_files(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            extension = os.path.splitext(filename)[1][1:]
            folder_name = os.path.join(folder_path, extension)

            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            shutil.move(os.path.join(folder_path, filename), os.path.join(folder_name, filename))

    print("Exit code = 0")
    
folder_path = askdirectory()
move_files(folder_path)
