new_word = "ubuntu"
old_word = "Root"
with open("data.txt", 'r') as read_mode:
    content = read_mode.read()

if old_word in content:
    print(f"'{old_word}' is present in the file.")
    with open("data.txt", 'w') as write_mode:
        updated_content = content.replace(old_word, new_word)
        write_mode.write(updated_content)

print("Updated file content:")
print(updated_content)
    