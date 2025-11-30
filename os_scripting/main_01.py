import os

dir_path = "/home/dixit/test1/"

def list_directory_contents(dir_path):
    contents = os.listdir(dir_path)
    for item in contents:
        print(item)


if __name__ == "__main__":   
    list_directory_contents(dir_path)
