first = int(input("Enter 1 number: "))
second = int(input("Enter 2 number: "))

your_name = input("Enter your name: ")

def greet(name):
    print(f"hello, ", name)

def avg(first_num, second_num):
    # a = int(input("Enter 1 number: "))
    # b = int(input("Enter 2 number: "))

    average = (first_num + second_num) / 2
    print(f"Average of these numbers is: {average} ")

avg(first, second)

greet(your_name)
