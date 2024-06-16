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
    index_of_contact = search(my_arr, contact)
    while index_of_contact == -1:
        contact = input("The name is not valid,Please enter another name:\n")
        list_contact(my_arr)
        index_of_contact = search(my_arr, contact)
    else:
        new_contact = input("Please enter the new name:\n")
        my_arr[index_of_contact] = new_contact
        print("the contact has been edited ,the index is ", index_of_contact, "\n")
    list_contact(my_arr)


def delete_contact(my_arr):  # works
    list_contact(my_arr)
    contact = input("Please enter name of contact\n")
    index_of_contact = search(my_arr, contact)
    while index_of_contact == -1:
        contact = input("The name is not valid,Please enter another name\n")
        index_of_contact = search(my_arr, contact)
    my_arr.remove(contact)
    print("the contact has been deleted\n")
    list_contact(my_arr)


def list_contact(my_arr):  # works
    my_arr.sort()
    # print(my_arr)
    for index, item in enumerate(my_arr):
        print(index, item)


def search(my_arr, contact_name):  # works
    index_of = -1
    for index, item in enumerate(my_arr):
        if contact_name == item:
            index_of = index
            print(index, item)
    return index_of


def menu():
    while True:
        print("1 - Add Contact")
        print("2 - Edit Contact")
        print("3 - Delete Contact")
        print("4 - List of all contacts")
        print("5 - Exit")
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
            print("Goodbye")
            break


menu()
