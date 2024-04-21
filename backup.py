import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    try:
        # Iterate over files in the source directory
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            
            # Check if the destination file already exists
            if os.path.exists(dest_path):
                # Append timestamp to filename to ensure uniqueness
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                filename, extension = os.path.splitext(filename)
                new_filename = f"{filename}_{timestamp}{extension}"
                dest_path = os.path.join(dest_dir, new_filename)
            
            # Copy file from source to destination
            shutil.copy2(source_path, dest_path)
            print(f"Copied '{filename}' to '{dest_path}'")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if correct number of command-line arguments provided
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    backup_files(source_dir, dest_dir)
