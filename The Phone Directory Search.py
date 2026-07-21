# Create a dictionary with 3 contacts

contacts = {
    "Lesedi": "0823568551",
    "Ofentse": "0794173554",
    "Lerato": "0815579417"
}

# Ask the user for the friend's name

name = input("Enter the name of the friend you want to look up: ").capitalize()

# Check if the contact exists

if name in contacts:
    print(f"Found! {name}'s number is {contacts[name]}.")
else:
    print("Contact not found.")