print("Hi there, this a a superuser gateway")
username = input("Username: ")


if username == "c4e":
    password = getpass.getpass("Password: ")
    if password == "codethechange":
        print("Welcome, c4e")
    else:
        print("Password is incorrect")
else:
    print("You are not superuser")

# import sys
# import msvcrt

# print('Enter your password: ')
# password = ''
# while True:
#     pressedKey = msvcrt.getch()
#     if pressedKey == '\r':    
#        break
#     else:
#         password = password + str(pressedKey)
#         sys.stdout.write('*')

# print('\n' + password)