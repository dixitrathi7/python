import os

# print the current working directory
print("Current Working Directory:")
print(os.getcwd())



# create a new directory 

new_dir = "new_folder"
dir_path = "/home/dixit/test1/"

full_path = os.path.join(dir_path, new_dir)
#os.mkdir(new_dir)    creates directory into current working directory

# if we create a single directory then we need to use mkdir
# but if we want to create multiple directories at a time then we need to use makedirs
if not os.path.exists(full_path):
    os.makedirs(full_path)
    print(f"Directory '{new_dir}' created successfully at {dir_path}.")
else:
    print(f"Directory '{new_dir}' already exists at {dir_path}.")




#print(f"Directory '{new_dir}' created successfully.")

# try:
#     os.mkdir(new_dir)
#     print(f"Directory '{new_dir}' created successfully.") 
# except FileExistsError:
#     print(f"Directory '{new_dir}' already exists.") 

