# 1. Write a Python program to print the number entered by user only if the number entered is negative.
num = int(input("Input number: "))

res = num < 0 or "num > 0"

print(res)

# 2. Write a Python program to check if the value a is less than 20 or not
print()

a = int(input("a = "))

res = a >= 20 or "a < 20"

print(res)

# 3. Write a Python program to check if a given number is Zero or Not.
print()

num = int(input("Input number: "))

res = num == 0 or "Given number is not 0"

print(res)

# 4. Write a Python program to check if a given number is Even or Odd.
print()

num = int(input("Input number: "))

res = num % 2 == 0 or "Given number is Odd"

print(res)

# 5. Write a Python program to find largest number among three numbers entered by user.
print()

a, b, c = int(input("a = ")), int(input("b = ")), int(input("c = "))

print("Largest number is", max(a, b, c))
