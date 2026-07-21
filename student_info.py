# Collect user information

first_name = input("Enter your first name: ") 
surname = input("Enter your surname: ")
age_years = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

# Combine names for greeting and formatting

full_name = f"{first_name} {surname}"

# Display greeting

name = input("Enter your name: ")
print(f"Welcome, {full_name}!")

# Display name in different formats

name = 'Lesedi Motshumi' 
print(name.upper())
print(name.title())

# Calculate age in months

age_years = int(input("Enter your age in years: "))
age_months = age_years * 12
print(f"Your age in months is: {age_months}")

# Round favourite number to 2 decimal places 

rounded_num = round(favourite_number, 2)
print(f"Your favourite number rounded to 2 decimal places is: {rounded_num}")

# Print data types

print("Data Types:")
print(f"first_name: {type(first_name)}")
print(f"age_years: {type(age_years)}")
print(f"favourite_number: {type(favourite_number)}")