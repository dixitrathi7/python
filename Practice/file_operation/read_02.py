
with open("data.txt", 'r') as read_mode:
    contente = read_mode.read()

if "twinekle" in contente:
    print("Yes! 'Twinekle' is present in the file.")
else:
    print("No! 'Twinekle' is not present in the file.")