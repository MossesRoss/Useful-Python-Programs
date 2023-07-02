import os
import shutil

def organize_files(directory):
    folders = {
        'Images': ['png', 'jpg', 'jpeg', 'gif'],
        'Documents': ['doc', 'docx', 'pdf', 'txt'],
        'Videos': ['mp4', 'avi', 'mov'],
        'Others': []
    }

    for filename in os.listdir(directory):
        if filename != 'organize_files.py': 
            file_extension = filename.split('.')[-1].lower()
            destination_folder = 'Others'  
          
            for folder, extensions in folders.items():
                if file_extension in extensions:
                    destination_folder = folder
                    break
            destination_path = os.path.join(directory, destination_folder)
            os.makedirs(destination_path, exist_ok=True)
            
            source_path = os.path.join(directory, filename)
            destination_file = os.path.join(destination_path, filename)
            shutil.move(source_path, destination_file)
            
            print(f"Moved '{filename}' to '{destination_folder}' folder.")


directory_to_organize = 'helpd/desktop'

organize_files(directory_to_organize)
