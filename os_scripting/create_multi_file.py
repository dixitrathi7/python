import os

source_path = "/home/dixit/test1/"

def create_multiple_files(dir_path, file_names):
    for file_name in file_names:
        full_path = os.path.join(dir_path, file_name)
        with open(full_path, 'w') as f:
            # f is temporary variable representing the opened file
            f.write(f"This is the content of {file_name}\n") # if need to Writing some content to the file
            #pass    # Just create an empty file
        print(f"File '{file_name}' created successfully at {dir_path}.")

file_names = ["file1.log", "file2.log", "file3.log", "file4.log", "file5.log"]

create_multiple_files(source_path, file_names)

