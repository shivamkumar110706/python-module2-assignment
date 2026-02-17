#Task 1: Perform Basic Mathematical Operations

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if  num2 != 0: #!= 'Not Equal'
    division = num1 / num2
else:
    division = "cannot divide by zero"

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
