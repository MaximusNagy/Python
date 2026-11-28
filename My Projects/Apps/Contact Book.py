contacts = {}

def con():
    print("\n--- Welcome to Contact eBook ---")
    print("1. Enter contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

while True:
    con()
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        name = input("Enter contact name: ").strip()
        phone = input("Enter contact number: ").strip()
        contacts[name] = phone
        print("✅ Contact added.")

    elif choice == "2":
        if contacts:
            print("\n📒 Contact List:")
            for name, phone in contacts.items():
                print(f"Name: {name} - Phone: {phone}")
        else:
            print("❌ No contacts found.")

    elif choice == "3":
        search_name = input("Enter name to search: ").strip()
        found = False
        for name, phone in contacts.items():
            if search_name.lower() in name.lower():
                print(f"🔎 Found: {name} - Phone: {phone}")
                found = True
        if not found:
            print("❌ Contact not found.")

    elif choice == "4":
        del_name = input("Enter name to delete: ").strip()
        if del_name in contacts:
            del contacts[del_name]
            print("🗑️ Contact deleted.")
        else:
            print("❌ Contact not found.")

    elif choice == "5":
        print("👋 Thanks for using Contact eBook!")
        break

    else:
        print("⚠️ Invalid option. Please choose a number between 1 and 5.")
