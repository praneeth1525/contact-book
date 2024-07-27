import json

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("Contact List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self, search_term):
        results = {name: details for name, details in self.contacts.items() 
                   if search_term.lower() in name.lower() or search_term in details['phone']}
        if not results:
            print("No contacts found.")
            return
        print("Search Results:")
        for name, details in results.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    def update_contact(self, name):
        if name not in self.contacts:
            print(f"Contact '{name}' not found.")
            return
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print(f"Contact '{name}' updated successfully.")

    def delete_contact(self, name):
        if name not in self.contacts:
            print(f"Contact '{name}' not found.")
            return
        del self.contacts[name]
        print(f"Contact '{name}' deleted successfully.")

    def save_to_file(self, filename="contacts.json"):
        with open(filename, "w") as file:
            json.dump(self.contacts, file)
        print(f"Contacts saved to {filename}")

    def load_from_file(self, filename="contacts.json"):
        try:
            with open(filename, "r") as file:
                self.contacts = json.load(file)
            print(f"Contacts loaded from {filename}")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty contact book.")

def main():
    contact_book = ContactBook()
    contact_book.load_from_file()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save Contacts")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
       
