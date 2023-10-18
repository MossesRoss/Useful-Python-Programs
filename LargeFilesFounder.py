import os
import shutil

def move_files_by_size(source_dir, destination_dir, min_file_size, max_file_size):
    # Ensure destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    min_file_size_bytes = min_file_size * (1024 ** 3)  # Convert GB to bytes
    max_file_size_bytes = max_file_size * (1024 ** 3)  # Convert GB to bytes

    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if min_file_size_bytes <= file_size <= max_file_size_bytes:
                shutil.move(file_path, destination_dir)

if __name__ == "__main__":
    source_directory = "source_directory"
    destination_directory = "/destination_directory"
    min_file_size_gb = 0.4
    max_file_size_gb = 4.0

    move_files_by_size(source_directory, destination_directory, min_file_size_gb, max_file_size_gb)
