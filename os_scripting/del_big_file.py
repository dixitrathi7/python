import os

dir_path = "/home/dixit/test1/"

max_size_bytes = 100 * 1024 * 1024  # 100MB

def delete_large_files(dir_path):

    for item in os.listdir(dir_path):
        full_path = os.path.join(dir_path, item)
        if os.path.isfile(full_path) and os.path.getsize(full_path) > max_size_bytes:
            os.remove(full_path)
            print(f"Deleted large file: {item}")

    print("Finished checking for large files.")

delete_large_files(dir_path)
