fav_items = ["chat", "girl", "something like that"]
fav_size = len(fav_items)
# for i, item in enumerate(fav_items):
#     print(i+1, item)


while True:
    command = input("What do you want (C, R, U, D)? ").upper()
    if command == "C":
        fav_new =  input("enter what is your fav? ")
        fav_items.append(fav_new)
        fav_size = len(fav_items)
        for i, item in enumerate(fav_items):
            print(i+1, item)
    elif command == "R":
    for i, item in enumerate(fav_items):
        print(i+1, item)
    elif command == "U":
        n = int(input("Which position do you want to replace? ")) - 1
        if 0 <= n < fav_size:
            fav_new = input("what is your favorite? ")

            fav_items[n] = fav_new

            print("*" * 20)
            for i in range(fav_size):
                print(i + 1, ". ", fav_items[i], sep = "")
            print("*" * 20)
        else:
            print("The position that you want to replace is out of the list. Please enter a number which is in range from 1 to", fav_size)
    elif command == "D":
        choice_del = input("Which one do you prefer, position or value of items (enter position or value)? ")
        if choice_del == "position":
            n = int(input("Which position do you want to delete? ")) - 1
            if 0 <= n < fav_size:
                fav_items.pop(n)
                fav_size_new = len(fav_items)
                print("*" * 20)
                for i in range(fav_size_new):
                    print(i + 1, ". ", fav_items[i], sep = "")
                print("*" * 20)
            else:
                print("The position that you want to delete is out of the list. Please enter a number which is in range from 1 to", fav_size)

        elif choice_del == "value":
            fav_del = (input("Which item do you want to delete? "))
            if fav_del in fav_items:
                fav_items.remove(fav_del)
                fav_size_new = len(fav_items)
                print("*" * 20)
                for i in range(fav_size_new):
                    print(i + 1, ". ", fav_items[i], sep = "")
                print("*" * 20)
            else:
                print("The item that you want to delete is out of the list. Please check the grammar again.")

        else:
            print("Please enter position or value!")
    else:
        print("Please choose the exactly letter on the list we provided.")