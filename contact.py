from os import system, name

def clear():
  system('cls' if name == 'nt' else 'clear')

def get_contact_info(favorite=False):
  name = input("Enter name: ")
  phone = input("Enter phone: ")
  email = input("Enter email: ")
  return {
    "name": name,
    "phone": phone,
    "email": email,
    "favorite": favorite
  }

def add_contact(contacts, new_contact):
  contacts.append(new_contact)
  print("Contact added successfully\n")
  return

def print_table(contacts):
  print("┌───┬──────────────┬──────────────┬──────────────┬──────────┐")
  print("│ # │    Name      │    Phone     │    Email     │ Favorite │")
  print("├───┼──────────────┼──────────────┼──────────────┼──────────┤")
  for index, contact in enumerate(contacts, start=1):
    contact_name = contact['name'][:9] + '...' if len(contact['name']) > 12 else contact['name']
    contact_phone = contact['phone'][:9] + '...' if len(contact['phone']) > 12 else contact['phone']
    contact_email = contact['email'][:9] + '...' if len(contact['email']) > 12 else contact['email']
    favorite = '[✓]' if contact['favorite'] else '[ ]'
    print(f"│ {index:<2}│ {contact_name:<12} │ {contact_phone:<12} │ {contact_email:<12} │{favorite:^10}│")
  print("└───┴──────────────┴──────────────┴──────────────┴──────────┘")

def view_contact_list(contacts):
  if not contacts:
    print("No contacts found\n")
  else:
    print_table(contacts)
  return

def get_contact_index(contacts):
  print_table(contacts)
  while True:
    try:
      index = int(input("Enter the number of the contact to select: "))
    except ValueError:
      print("Invalid input. Please enter a number.\n")
      continue
    if index < 1 or index > len(contacts):
      print("Invalid contact number\n")
    else:
      break
  return index - 1

def edit_contact(contacts, index, new_contact):
  contacts[index] = new_contact
  print("Contact updated successfully\n")
  return

def mark_contact_as_favorite(contacts, index):
  contacts[index]['favorite'] = True
  print("Contact marked as favorite\n")
  return

def remove_favorite_contact(contacts, index):
  contacts[index]['favorite'] = False
  print("Contact removed from favorites\n")
  return

def view_favorite_contacts(contacts):
  favorite_contacts = [contact for contact in contacts if contact['favorite']]
  if not favorite_contacts:
    print("No favorite contacts found\n")
  else:
    print_table(favorite_contacts)
  return

def delete_contact(contacts, index):
  contacts.pop(index)
  print("Contact deleted successfully\n")
  return

clear()
contacts = []
while True:
  print("╔════════════════════════════════╗")
  print("║        Contact Agenda          ║")
  print("╠════════════════════════════════╣")
  print("║ 1. Add contact                 ║")
  print("║ 2. View contact list           ║")
  print("║ 3. Edit contact                ║")
  print("║ 4. Mark contact as favorite    ║")
  print("║ 5. Remove favorite contact     ║")
  print("║ 6. View favorite contacts      ║")
  print("║ 7. Delete contact              ║")
  print("║ 8. Exit                        ║")
  print("╚════════════════════════════════╝")

  choice = input("Enter your choice: ")

  print()

  match choice:
    case "1":
      add_contact(contacts, get_contact_info())
    case "2":
      view_contact_list(contacts)
    case "3":
      edit_contact(contacts, get_contact_index(contacts), get_contact_info())
    case "4":
      mark_contact_as_favorite(contacts, get_contact_index(contacts))
    case "5":
      remove_favorite_contact(contacts, get_contact_index(contacts))
    case "6":
      view_favorite_contacts(contacts)
    case "7":
      delete_contact(contacts, get_contact_index(contacts))
    case "8":
      break
    case _:
      print("Invalid choice\n")

  input("Press Enter to continue...")
  clear()
