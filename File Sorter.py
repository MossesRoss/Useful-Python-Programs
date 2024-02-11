import os
import shutil

def organize_files(directory):
    directories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Music": [".mp3", ".wav"],
        "Others": []
    }

    for folder in directories:
        if not os.path.exists(os.path.join(directory, folder)):
            os.mkdir(os.path.join(directory, folder))

    # Organize files
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            file_extension = os.path.splitext(file)[1]
            for folder, extensions in directories.items():
                if file_extension.lower() in extensions:
                    shutil.move(os.path.join(directory, file), os.path.join(directory, folder, file))
                    break

def main():
    directory = input("Enter the directory path to organize: ")
    organize_files(directory)
    print("Files organized successfully.")

if __name__ == "__main__":
    main()
