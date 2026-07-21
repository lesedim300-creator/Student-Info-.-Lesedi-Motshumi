# Secure Password Hint Tool

# Ask the user for their password

password = input("Enter your secret password: ")

# Remove leading and trailing spaces

password = password.strip()

# Get the first and last letters

first_letter = password[0]
last_letter = password[-1]

# Display the password hint using an f-string

print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}.")