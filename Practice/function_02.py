

def arg(name, age=24):  # 24 is default value of age if user not provide any value
    print(f"Hello {name}, you are {age} year old")
    return "thanks for using this function"


a = arg("Dixit", 28)
print(a)