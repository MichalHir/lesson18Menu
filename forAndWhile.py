def zugi(my_arr):  # ran
    return_arr = []
    for item in my_arr:
        if item % 2 == 0:
            return_arr.append(item)
    return return_arr


print(zugi([1, 2, 3, 4]))  # ran


list_arr = [6, 7, 3, 9, 7]


def biggest(my_arr):
    bigger = my_arr[0]
    for i in my_arr:
        bigger = max(bigger, i)
    return bigger


print(biggest(list_arr))
print(biggest([1, 9, 240, 6]))
print(biggest([5, 4, 3, 1]))
print(biggest(["a", "baa", "c", "zzz"]))
print(biggest("HELLO"))
# print(biggest([1,'a',2,'b']))

# i = 1 #ran
# while i < 6:
#   print(i)
#   i += 1

while True:  # ran -true means endless loop until break
    my_number = int(input("please enter a number "))
    print("your number is", my_number)
    if my_number == 0:
        break


def menu():
    print(
        """1 - add contact
    2 - remove contact
    3 - edit contact
    4 - list contacts
    5 - exit
    """
    )
    input_num = input("enter your choice by number")
    while True:
        if input_num == "1":
            print("you chose add contact")
            input_num = input("enter your choice by number")
        if input_num == "2":
            print("you chose remove contact")
            input_num = input("enter your choice by number")
        if input_num == "3":
            print("you chose edit contact")
            input_num = input("enter your choice by number")
        if input_num == "4":
            print("you chose list contacts")
            input_num = input("enter your choice by number")
        if input_num == "5":
            print("you chose exit")
            break
menu()

