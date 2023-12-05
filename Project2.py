# Project 2
# Name:
# Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the contacts. The program will have the following features:
# 1. Add contact
# 2. View contacts
# 3. Delete contact
# 4. Save contacts to csv file
# 5. Next Birthday
# 0. Quit

# Import the csv module, datetime module
import csv
import datetime as dt

# Make sure to show docs strings for each function and include comments in your code. Make sure to include a main function and call the main function at the end of the program.

print("Welcome to the Contact List Program")

# There is also a contact.csv file that will be used to store the contacts. The csv file will have the following format:
# Name,Phone,Email,Birthday
# The program will be menu driven and will display the menu as shown above. The program will run until the user selects option 0 to quit. The program will be implemented in a file called Project2.py. The program will use the following functions:


# import_csv - This function will import the contacts from the csv file. The function will return a dictionary of contacts. The key will be the name of the contact and the value will be a dictionary containing the phone number, email address, and birthday. The function will take one parameter, the name of the csv file. The function will display an error message if the file does not exist. The function will display a message if the file exists and the contacts were imported successfully.
# Hint1: Use the csv module to read the csv file. Use the csv.reader function. IE. reader = csv.reader(file)
# Hint2: You will need to skip the first line of the csv file since it contains the column headers. You can do that with the next function. IE. next(reader)
# Hint3: You will need to create a dictionary of contacts. You can do that by looping through the reader object. IE. for row in reader:
# Hint4: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(row[3], '%m/%d/%Y')
# Hint5: You will need to create a dictionary of the phone number, email address, and birthday. You can do that by creating a dictionary and adding the values to the dictionary. IE. contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
# Hint6: Use the FileNotFoundError exception to catch if the file does not exist.


def import_csv(file_name):
    """
    Import contacts from a CSV file and return a dictionary of contacts.

    :param file_name: The name of the CSV file.
    :return: A dictionary of contacts.
    """
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            contacts = {}
            for row in reader:
                name = row[0]
                phone = row[1]
                email = row[2]
                birthday = dt.datetime.strptime(row[3], '%m/%d/%Y')
                
                contacts[name] = {'Phone': phone, 'Email': email, 'Birthday': birthday}

        print(f"Contacts imported successfully from {file_name}.")
        return contacts

    except FileNotFoundError:
        print(f"Error: {file_name} not found. No contacts imported.")
        return {}

# Test the function
file_name = "contacts\.csv"
contacts_dict = import_csv(file_name)
print(contacts_dict)




# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. The function will take four parameters, the name, phone number, email address, and birthday. The function will return True if the contact was added and False if the contact was not added. The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]


def add_contact(contacts, name, phone, email, birthday, csv_file):
    """
    Add a contact to the dictionary of contacts and update the CSV file.

    :param contacts: The dictionary of contacts.
    :param name: The name of the new contact.
    :param phone: The phone number of the new contact.
    :param email: The email address of the new contact.
    :param birthday: The birthday of the new contact in the format '%m/%d/%Y'.
    :param csv_file: The name of the CSV file to update.
    :return: True if the contact was added, False if the contact already exists.
    """
    # Convert the birthday to a datetime object
    birthday_datetime = dt.datetime.strptime(birthday, '%m/%d/%Y')

    # Check if the contact already exists
    if name in contacts:
        print(f"Error: Contact '{name}' already exists. Contact not added.")
        return False
    else:
        # Add the new contact to the dictionary
        contacts[name] = {'Phone': phone, 'Email': email, 'Birthday': birthday_datetime}
        print(f"Contact '{name}' added successfully.")

        # Update the CSV file
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email', 'Birthday'])  # Write header row

            for contact_name, details in contacts.items():
                phone = details['Phone']
                email = details['Email']
                birthday = details['Birthday'].strftime('%m/%d/%Y')
                writer.writerow([contact_name, phone, email, birthday])

        return True




def add_contact(contacts, name, phone, email, birthday):





    """
    Add a contact to the dictionary of contacts.

    :param contacts: The dictionary of contacts.
    :param name: The name of the new contact.
    :param phone: The phone number of the new contact.
    :param email: The email address of the new contact.
    :param birthday: The birthday of the new contact in the format '%m/%d/%Y'.
    :return: True if the contact was added, False if the contact already exists.
    """
    # Convert the birthday to a datetime object
    birthday_datetime = dt.datetime.strptime(birthday, '%m/%d/%Y')

    # Check if the contact already exists
    if name in contacts:
        print(f"Error: Contact '{name}' already exists. Contact not added.")
        return False
    else:
        # Add the new contact to the dictionary
        contacts[name] = {'Phone': phone, 'Email': email, 'Birthday': birthday_datetime}
        print(f"Contact '{name}' added successfully.")
        return True

# Example usage:
contacts_dict = import_csv("contacts.csv")  # Assuming you have imported contacts from the CSV file
add_contact(contacts_dict, "Jorge Gonzales", "123-456-7890", "Jorgegonzales191421@Gmail.com", "01/01/2001")

print(contacts_dict)


# view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.
# Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():
# Extra Credit: The data is a dictionary of dictionaries. You can unpack the dictionary into a list of dictionaries. Like in Lab 10 and then use the tabulate library to display the contacts in a table format. This is optional and not required. You can use string formatting to display the contacts in a table format.
from tabulate import tabulate

def view_contacts(contacts):
    """
    Display the contacts in a formatted table using the tabulate library.

    :param contacts: The dictionary of contacts.
    :return: None
    """
    # Check if there are no contacts in the dictionary
    if not contacts:
        print("No contacts available.")
        return

    # Convert the contacts dictionary into a list of dictionaries
    data = [{"Name": name, **details} for name, details in contacts.items()]

    # Print the table using tabulate
    print(tabulate(data, headers="keys", tablefmt="psql"))

# Example usage:
contacts_dict = import_csv("contacts.csv")  # Assuming you have imported contacts from the CSV file
view_contacts(contacts_dict)



# delete_contact(id) - This function will delete a contact from the dictionary. The function will take one parameter, the name of the contact to delete. The function will return True if the contact was deleted and False if the contact was not deleted. The function will display an error message if the contact does not exist.




# next_birthday() - This function will display the next birthday. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. The function will display a message if there are no birthdays in the next 30 days. The function will display the next birthday and name if there is a birthday in the next 30 days. Use string formatting to display the next birthday. The next birthday should be sorted by the next birthday. The next birthday should be formatted as mm/dd/yyyy.
# Hint: We dont care about the year, only the month and day. There are many ways to solve this issue. 1st you could replace all the years with the current year.2nd you could use the month and day attributes of the datetime object to compare the month and day of the birthday to the current month and day.

# save_csv(filename) - This function will save the contacts to the csv file. Prompt the user to enter a filename to save the contacts to. If the file exists, overwrite the file. If the file does not exist, create the file. The function will return True if the contacts were saved and False if the contacts were not saved.

# The main function will be used to run the program. The main function will use a while loop to display the menu and get the user's choice. The main function will call the appropriate function based on the user's choice. The main function will also call the save_csv function to save the contacts to the csv file before the program ends.


def main():
    """Add Code here to call the functions and run the program"""
    pass  # Remove this line when you start writing your code

    # After you are done with the program, answer the following questions using code (show your code and output):
    # How many names start with the letter A?

    # How many emails are yahoo emails?

    # How many .org emails are there?

    # How many contacts have a birthday in January?


if __name__ == "__main__":
    main()
