import os

dir_path = "/home/dixit/"

def del_empty_file(dir_path):

    for item in os.listdir(dir_path):
        full_path = os.path.join(dir_path, item)

        if os.path.isfile(full_path) and os.path.getsize(full_path) == 0:
            os.remove(full_path)
            print(f"Deleted empty file: {full_path}")

del_empty_file(dir_path)
