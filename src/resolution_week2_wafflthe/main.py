import argparse
import sys
import os
import json

CONTACTS = "Contacts.json"
version = "1.0.2"

def load_contacts():
    if not os.path.exists(CONTACTS):
        return[]
    with open(CONTACTS, "r") as file:
        return json.load(file)
    
def add_contact(contact):
    with open(CONTACTS, "w") as file:
        json.dump(contact, file, indent=2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", nargs=2, metavar=("Name", "Email"), help="Add new contact and email")
    parser.add_argument("-l", "--list", help="List all contacts", action="store_true")
    parser.add_argument("-d", "--delete", type=int, help="Delte contact with ID")
    parser.add_argument("-i", "--info", action="store_true", help="Info about app and usage")
    args = parser.parse_args()

    if args.add:
        contact = load_contacts()   
        name, email = args.add
        if len(contact) == 0:
            id = 1
        else:
            id = contact[-1]["id"] + 1
        contact.append({"id": id, "name": name, "Email":  email})
        add_contact(contact)
        print(f"{name} was added to contacts with email: {email}")

    if args.delete:
        contacts = load_contacts()
        new_contact = []
        for contact in contacts:
            if contact["id"] != args.delete:
                new_contact.append(contact)  
        contacts = new_contact
        add_contact(contacts)
        print(f"Contact number {args.delete} was deleted")

    if args.list:
        contacts = load_contacts()
        if not contacts:
            print("╔════════════Contacts═══════════╗")
            print("║ Aw no contacts yet, add w -a! ║")
            print("╚═══════════════════════════════╝")
        else:
            print("╔════════════Contacts═══════════╗")
            for contact in contacts:
                print(f"[{contact['id']}] {contact['name']}: {contact['Email']}")
            print("╚═══════════════════════════════╝")

    if args.info:
        print(f"╔══════════════════════════════╗")
        print(f"║  Contact list ver {version}      ║")
        print(f"║ -a/--add adds a new contact  ║")
        print(f"║type name and email with space║")
        print(f"║ between the two after to add ║")
        print(f"║-d/--delete to delete contact ║")  
        print(f"║   type contact id to select  ║")
        print(f"║  -l to show list of contacts ║")
        print(f"╚══════════════════════════════╝")
if __name__ == "__main__":
    main()
