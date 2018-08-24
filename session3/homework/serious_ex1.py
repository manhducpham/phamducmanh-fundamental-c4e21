shop_items = ["T-shirt", "Sweater"]
shop_size = len(shop_items)
print()
while True:
    print()
    command = input('''Welcome to our shop, what do you want (C, R, U, D)? 
(Enter "exit" to end the program)
Your choice is: ''').lower()
    print()
    if command == "c":
        shop_new =  input("Enter new item: ").capitalize()
        shop_items.append(shop_new)
        print("*" * 40)
        print("Our items:", end =" ")
        print(*shop_items, sep = ", ")
        print("*" * 40)
        print()

    elif command == "r":
        print("*" * 40)
        print("Our items:", end =" ")
        print(*shop_items, sep = ", ")
        print("*" * 40)
        print()

    elif command == "u":
        n = int(input("Update position? ")) - 1
        if 0 <= n < shop_size:
            shop_new = input("New item? ").capitalize()
            shop_items[n] = shop_new
            print("*" * 40)
            print("Our items:", end =" ")
            print(*shop_items, sep = ", ")
            print("*" * 40)
            print()
        else:
            print("The position that you want to replace is out of our item list. Please enter a number which is in range from 1 to", shop_size)
            print()
    
    elif command == "d":
        while True:
            choice_del = input('''Which one do you prefer, position or value of items (enter position or value)? 
Enter "back" to go to previous menu
Your choice is: ''').lower()
            if choice_del == "position":
                n = int(input("Delete position? ")) - 1
                if 0 <= n < shop_size:
                    shop_items.pop(n)
                    shop_size_new = len(shop_items)
                    print("*" * 40)
                    print("Our items:", end =" ")
                    print(*shop_items, sep = ", ")
                    print("*" * 40)
                    print()
                else:
                    print("The position that you want to delete is out of the list. Please enter a number which is in range from 1 to", shop_size)
                    print()

            elif choice_del == "value":
                shop_del = (input("Delete item? "))
                if shop_del in shop_items:
                    shop_items.remove(shop_del)
                    shop_size_new = len(shop_items)
                    print("*" * 40)
                    print("Our items:", end =" ")
                    print(*shop_items, sep = ", ")
                    print("*" * 40)
                    print()
                
                else:
                    print("The item that you want to delete is out of the list. Please check the grammar again.")
                    print()
            elif choice_del == "back":
                    break
            else:
                print("Please enter position or value!")
                print()
    
    elif command == 'exit':
        break
    else:
        print("Sorry for the inconvenience to you. Please try again. Choose one in the list we provided.")
        print()