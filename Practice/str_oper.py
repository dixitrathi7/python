
def update(list1, word):
    new_list = []
    for item in list1:
        if not(item == word):
            new_list.append(item.strip(word))
        return new_list
    

list1 = ['apple', 'banana', 'cherry', 'date', 'apple']
word = 'apple'
result = update(list1, word)
print(result)  # Output should be ['banana', 'cherry', 'date']

