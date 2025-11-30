# write a program to print 5 tables

# for i in range(1, 11):
#     result = 5 * i
#     print(f"5 X {i} = ", result)


# --- IGNORE ---
# print odd and even numbers from range


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Here is the list of even numbers:")
for i in range(start, end + 1):
    if i % 2 == 0:
        print(f"{i} is even")
print("\n")

print(f"Here is the list of odd numbers:")
for i in range(start, end + 1):
    if i % 2 != 0:
        print(f"{i} is odd")