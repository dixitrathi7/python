import os

dir_path = "/home/dixit/"
#dir_path = "C:\Users\Dixit Rathi\Documents\my_github_repo\python\os_scripting"

print(f"Contents of the directory '{dir_path}':")

#contents = os.listdir(dir_path)  list all files and directories into the provided path
# for item in contents:
#     print(item)


for item in os.listdir(dir_path):
    full_path = os.path.join(dir_path, item) 
    if os.path.isfile(full_path) and item.endswith(".pem"):
        print(f"File: {item}")


