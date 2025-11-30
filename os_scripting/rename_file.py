import os

dir_path = "/home/dixit/"

old_name = "testing.txt"
new_name = "test.txt"

old_path = os.path.join(dir_path, old_name)
new_path =  os.path.join(dir_path, new_name)

if os.path.exists(old_path):
    os.rename(old_path, new_path)
    print(f"Renamed '{old_name}' to '{new_name}' successfully")

else:
    print(f"The file '{old_name}' does not exist.")