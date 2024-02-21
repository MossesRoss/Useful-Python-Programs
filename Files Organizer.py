import os
import shutil

photo_extensions = [".jpg", ".jpeg", ".png", ".gif"]
video_extensions = [".mp4", ".avi", ".mov", ".wmv"]
document_extensions = [".pdf", ".docx", ".doc", ".xlsx", ".pptx"]
other_extensions = [".txt", ".zip", ".rar", ".exe"]

#Define source
source_folder = "/path/to/your/source/folder"
photo_folder = os.path.join(source_folder, "Photos")
video_folder = os.path.join(source_folder, "Videos")
document_folder = os.path.join(source_folder, "Documents")
other_folder = os.path.join(source_folder, "Other")

for folder in [photo_folder, video_folder, document_folder, other_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

for root, _, files in os.walk(source_folder):
    for filename in files:
        filepath = os.path.join(root, filename)
        extension = os.path.splitext(filename)[1].lower()

        if extension in photo_extensions:
            destination = photo_folder
        elif extension in video_extensions:
            destination = video_folder
        elif extension in document_extensions:
            destination = document_folder
        else:
            destination = other_folder
          
        try:
            shutil.move(filepath, os.path.join(destination, filename))
            print(f"Moved {filename} to {destination}")
        except Exception as e:
            print(f"Error moving {filename}: {e}")

print("File organization complete!")
