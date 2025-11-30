def recursion(n):
    if (n ==1 or n == 0):
        return 1
    else:
        return n * recursion(n - 1)

a = int(input("Enter a number to find its factorial: ")) 
print(f"Factorial of {a} is: {recursion(a)}")
