import json


CONTACT_FILE_PATH = "contacts.json"


def read_contacts(file_path):
    try:
        with open(file_path, 'r') as f:
            contacts = json.load(f)['contacts']
    except FileNotFoundError:
        contacts = []

    return contacts


def write_contacts(file_path, contacts):
    with open(file_path, 'w') as f:
        contacts = {"contacts": contacts}
        json.dump(contacts, f)


def verify_email_address(email):
    if "@" not in email:
        return False

    split_email = email.split("@")
    identifier = "".join(split_email[:-1])
    domain = split_email[-1]

    if len(identifier) < 1:
        return False

    if "." not in domain:
        return False

    split_domain = domain.split(".")

    for section in split_domain:
        if len(section) == 0:
            return False

    return True

def verify_name(name):
    if len(name) == 0:
        return False
    else:
        return True

def add_contact(contacts):
    contact = {}
    error_status = False

    name = input("First Name: ")
    last_name = input("Last Name: ")
    mobile_phone_number = input("Mobile Phone Number: ")
    home_phone_number = input("Home Phone Number: ")
    email = input("Email Address: ")
    address = input("Address: ")

    if (any((d["name"] == name and d["last_name"] == last_name) for d in contacts)): #checks if name+surname exists in single contact dictionary
        print("A contact with this name already exists.")
        error_status = True

    if len(mobile_phone_number) != 0 and (not mobile_phone_number.isnumeric() or len(mobile_phone_number)!=9):
        print("Invalid mobile phone number.")
        error_status = True

    if len(home_phone_number) != 0 and (not home_phone_number.isnumeric() or len(home_phone_number)!=9):
        print("Invalid home phone number.")
        error_status = True

    if len(email) != 0 and (not verify_email_address(email)):
        print("Invalid email address.")
        error_status = True
    
    if error_status:
        print("You entered invalid information, this contact was not added.")
    else:
        contact = {"name":name, "last_name":last_name, "mobile_phone_number":mobile_phone_number, "home_phone_number":home_phone_number, "email":email, "address":address}
        contacts.append(contact)
        write_contacts(CONTACT_FILE_PATH, contacts)
        print("\nContact added!")

def search_for_contact(contacts):
    
    name_to_search = input("First name: ").lower()
    last_name_to_search = input("Last name: ").lower()
    result_contacts_lst = []

    for contact in contacts:
        if name_to_search in contact["name"].lower() and last_name_to_search in contact["last_name"].lower():
            result_contacts_lst.append(contact)


    for i, contact in enumerate(result_contacts_lst):
        print(f"{i+1}. {contact['name']} {contact['last_name']}")

        if len(contact["mobile_phone_number"]) > 0:
            print(f"\tMobile: {contact['mobile_phone_number']}")
        if len(contact["home_phone_number"]) > 0:
            print(f"\tHome: {contact['home_phone_number']}")
        if len(contact["email"]) > 0:
            print(f"\tEmail: {contact['email']}")
        if len(contact["address"]) > 0:
            print(f"\tAddress: {contact['address']}")

def delete_contact(contacts):
    name_to_delete = input("First name: ")
    last_name_to_delete = input("Last name: ")
    index = None
    deletion = False

    for i, contact in enumerate(contacts):
        if contact["name"] == name_to_delete and contact["last_name"] == last_name_to_delete:
            index = i
            deletion = True
            break
        else:
            continue

    if not deletion:
        print("No contact with this name exists.")
        return

    if deletion:
        while True:
            user_input = input("Are you sure you would like to delete this contact (y/n)? ").lower()
            if user_input == "y":
                contacts.pop(index)
                write_contacts(CONTACT_FILE_PATH, contacts)
                print("\nContact deleted!")
                break
            elif user_input == "n":
                print("\nContact deletion cancelled.")
                break
            else:
                print('Please answer "y" or "n".')
                continue
            

def list_contacts(contacts):
    for i, contact in enumerate(contacts):
        print(f"{i+1}. {contact['name']} {contact['last_name']}")

        if len(contact["mobile_phone_number"]) > 0:
            print(f"\tMobile: {contact['mobile_phone_number']}")
        if len(contact["home_phone_number"]) > 0:
            print(f"\tHome: {contact['home_phone_number']}")
        if len(contact["email"]) > 0:
            print(f"\tEmail: {contact['email']}")
        if len(contact["address"]) > 0:
            print(f"\tAddress: {contact['address']}")

def main(contacts_path):
    contacts = read_contacts(CONTACT_FILE_PATH)

    print("""
    Welcome to your contact list!
    The following is a list of useable commands:
    "add": Adds a contact.
    "delete": Deletes a contact.
    "list": Lists all contacts.
    "search": Searches for a contact by name.
    "q": Quits the program and saves the contact list.""")

    command_list = ["add", "delete", "list", "search", "q"]
    
    while True:

        user_input = input("\nType a command: ").lower()

        if user_input not in command_list:
            print("This is not a valid command. Please try again!")
            continue

        if user_input == "add":
            add_contact(contacts)

        elif user_input == "delete":
            delete_contact(contacts)

        elif user_input == "list":
            list_contacts(contacts)

        elif user_input == "search":
            search_for_contact(contacts)

        elif user_input == "q":
            write_contacts(CONTACT_FILE_PATH, contacts)
            print("Contacts were saved successfully.")
            break

if __name__ == "__main__":
    main(CONTACT_FILE_PATH)
