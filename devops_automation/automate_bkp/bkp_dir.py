import shutil
import os
from datetime import datetime

def bkp_directory(source_dir, destination_dir):

    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Create a timestamped backup filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_filename = f"backup_{timestamp}"

    backup_filepath = os.path.join(destination_dir, backup_filename)

    # Create a zip archive of the source directory
    shutil.make_archive(base_name=backup_filepath.replace('.zip', ''), format='zip', root_dir=source_dir)
    #shutil.make_archive(backup_filepath, 'zip', source_dir)

    print(f"Backup of '{source_dir}' created at '{backup_filepath}'")
    return backup_filepath

source_directory = "/home/dixit/"
destination_directory = "/home/dixit/backup/"

bkp_directory(source_directory, destination_directory)

