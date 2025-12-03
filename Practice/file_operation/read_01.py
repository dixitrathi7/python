with open("data.txt", 'a') as write_mode:
    write_mode.write("now i can able to add the content \n")

with open("data.txt", 'r') as read_mode:
    content = read_mode.read()
    print(content)