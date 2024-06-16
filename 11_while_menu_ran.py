my_contacts = []


#  לסיים את ספר הטלפונים כולל חיפוש
# :להוסיף עוד פונקציה מעניינת כגון
# a תן לי את כל אנשי הקשר באות
# מיין את המערך
# הוסף רשימה של מועדפים וכולי


def add_contact(my_arr):  # works
    new_contact = input("please enter name of new contact:\n")
    my_arr.append(new_contact)
    print("the contact has been added\n")
    list_contact(my_arr)


def edit_contact(my_arr):  # works
    list_contact(my_arr)
    contact = input("Please enter name of contact you would like to edit:\n")
    index_of_contact = simple_search(my_arr, contact)
    while index_of_contact == -1:
        contact = input("The name is not valid,Please enter another name or enter 7 to return to menu:\n")
        if contact =="7":
            menu()
            break
        list_contact(my_arr)
        index_of_contact = simple_search(my_arr, contact)
    else:
        new_contact = input("Please enter the new name:\n")
        my_arr[index_of_contact] = new_contact
        print("the contact has been edited ,the index is ", index_of_contact, "\n")
    list_contact(my_arr)


def delete_contact(my_arr):  # works
    list_contact(my_arr)
    contact = input("Please enter name of contact\n")
    index_of_contact = simple_search(my_arr, contact)
    while index_of_contact == -1:
        contact = input("The name is not valid,Please enter another name or enter 7 to return to menu\n")
        if contact =="7":
            menu()
            break
        index_of_contact = simple_search(my_arr, contact)
    my_arr.remove(contact)
    print("the contact has been deleted\n")
    list_contact(my_arr)


def list_contact(my_arr):  # works
    if my_arr==[]:
        print("there no contacts to display")
    my_arr.sort()
    for index, item in enumerate(my_arr):
        print(index, item)


def simple_search(my_arr, contact_name):  # works
    index_of = -1
    for index, item in enumerate(my_arr):
        if contact_name == item:
            index_of = index
            print(index, item)
    return index_of
def search_part_word(my_arr, contact_name):
    # casefold()	Converts string into lower case
    # lower()	Converts a string into lower case
    # find()	Searches the string for a specified value and returns the position of where it was found
    index_of = -1
    if_contains=False
    for index, item in enumerate(my_arr):
        if (item.lower()).find(contact_name.lower())>=0:
            if_contains=True
            index_of=index
            print(index,item)
    if if_contains==False:
        print("no search results\n")

def menu():
    while True:
        print("1 - Add Contact")
        print("2 - Edit Contact")
        print("3 - Delete Contact")
        print("4 - List of all contacts")
        print("5 - search")
        print("6 - Exit")
        selection = input("please enter command:\n")
        if selection == "1":
            add_contact(my_contacts)
        if selection == "2":
            edit_contact(my_contacts)
        if selection == "3":
            delete_contact(my_contacts)
        if selection == "4":
            list_contact(my_contacts)
        if selection == "5":
            contact = input("Please enter name of contact\n")
            search_part_word(my_contacts,contact)
        if selection == "6":
            print("Goodbye")
            break


menu()
