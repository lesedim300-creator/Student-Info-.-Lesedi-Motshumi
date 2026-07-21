# Collect two numbers from the user

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations

addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

# Display results

print("Calculator results")
print(f"Addition  : {addition}")
print(f"Subtraction  : {subtraction}")
print(f"Multiplication  : {multiplication}")

# Handle division by zero

try:
     division = round(num1 / num2, 2)
     floor_division = num1 // num2
     modulus = round(num1 % num2, 2)

     print(f"Division  : {division}")
     print(f"Floor Division  : {floor_division}")
     print(f"Modulus  : {modulus}")

except ZeroDivisionError:
     print("Error  : Cannot divide, floor divide, or modulus by zero.")
     
