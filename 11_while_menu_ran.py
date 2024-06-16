my_contacts = []

#  לסיים את ספר הטלפונים כולל חיפוש
# :להוסיף עוד פונקציה מעניינת כגון  
# a תן לי את כל אנשי הקשר באות 
# מיין את המערך
# הוסף רשימה של מועדפים וכולי
def add_contact(my_arr):
    new_contact = input("please enter name of new contact:")
    my_arr.append(new_contact)


def edit_contact(my_arr):
    list_contact(my_arr)
    contact = input("Please enter name of contact you would like to edit")
    while contact in my_arr==False:
        contact = input("The name is not valid,Please enter another name")
    new_contact = input("Please enter the new name")
    # index = my_arr.lo(contact)
    # my_arr.insert(index, new_contact)


def delete_contact(my_arr):
    list_contact(my_arr)
    contact = input("Please enter name of contact")
    while contact in my_arr==False:
        contact = input("The name is not valid,Please enter another name")
    my_arr.remove(contact)


def list_contact(my_arr):
    # my_arr.sort()
    print(my_arr)


def menu():
    while True:
        print("1 - Add Contact")
        print("2 - Edit Contact")
        print("3 - Delete Contact")
        print("4 - List of all contacts")
        print("5 - Exit")
        selection = input("please enter command:")
        if selection == "1":
            add_contact(my_contacts)
        if selection == "2":
            edit_contact(my_contacts)
        if selection == "3":
            delete_contact(my_contacts)
        if selection == "4":
            list_contact(my_contacts)
        if selection == "5":
            break


menu()
