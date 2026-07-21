contacts = []

def add_contacts():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email 
    }

    contacts.append(contact)
    print("Contact added successfully!")

def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower(): 
            return contact
        return None

def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return 
        print("Contact not found.")

def view_all():
    if not contacts:
        print("No contacts available.")
        return
    
    print("Contact List")
    for contact in contacts:
        print(f"Name : {contact['name']}")
        print(f"Phone : {contact['phone']}")
        print(f"Email : {contact['email']}")
        print("-"* 20)

while True:
    print("Contact Book Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contacts()

    elif choice == "2":
        name = input("Enter contact name to search: ")
        result = search_contact(name)

        if result:
            print("Contact Found:")
            print(f"Name : {result['name']}")
            print(f"Phone : {result['phone']}")
            print(f"Email : {result['email']}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter contact name to delete: ")
        delete_contact(name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("Exiting Contact Book. Goodbye! ") 
        break

    else:
            print("Invalid choice. Please enter a number between 1 and 5.")    
        