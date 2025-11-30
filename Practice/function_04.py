
def great(a, b, c):
    """
    This function takes three numbers and returns the greatest among them.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
        
    

x = int(input("Enter 1 number: "))
y = int(input("Enter 2 number: "))
z = int(input("Enter 3 number: "))
    

#great(x, y, z)
result = great(x, y, z)
print("The greatest number is:", result)