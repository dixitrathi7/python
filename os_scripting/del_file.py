import os

dir_path = "/home/dixit/test1/"

def delete_empty_files(dir_path):

    for item in os.listdir(dir_path):
        full_path = os.path.join(dir_path, item)
        if os.path.isfile(full_path) and item.endswith(".log"):
            os.remove(full_path)
            # if os.path.getsize(full_path) == 0:  # only you want to deletre empty files
            #     os.remove(full_path)
            #     print(f"Deleted empty log file: {item}")

    print("Finished checking for empty .log files.")

delete_empty_files(dir_path)

