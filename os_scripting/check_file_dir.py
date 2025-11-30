import os

real_path = "/home/dixit/test.txt"

if os.path.exists(real_path):
    print(f"The path '{real_path}' exists.")

    if os.path.isfile(real_path):
        print(f"'{real_path}' is a file.")
    elif os.path.isdir(real_path):
        print(f"'{real_path}' is a directory.")
else:
    print(f"The path '{real_path}' does not exist.")

