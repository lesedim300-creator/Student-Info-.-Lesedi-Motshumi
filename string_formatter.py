# Collect user input

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio: ")

#Create username

username = first_name[0].lower() + last_name.lower()

# Display full name in Title Case

full_name = f"{first_name} {last_name}".title()

# Remove leading/trailing spaces from bio

clean_bio = bio.strip()

# Count characters in the bio

bio_length = len(clean_bio)

# Replace "I am" with "I'm"

updated_bio = clean_bio.replace("I am", "I'm")

# Display output using f-strings

print(f"User Profile")
print(f"Full Name: {full_name}")
print(f"Username: {username}")
print(f"Bio: {updated_bio}")
print(f"Number of characters in bio: {bio_length}")