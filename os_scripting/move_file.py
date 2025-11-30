import os

def move_file(so_path, dist_path):
    os.rename(so_path, dist_path)
    print(f"File moved from '{so_path}' to '{dist_path}'")

so_path = "/home/dixit/test.txt"
dist_path = "/home/dixit/test1/test.txt"

move_file(so_path, dist_path)