# bai toan tra cuu lookup
v1 = {
    "lol": "laugh out loud",
    'anw': "any way",
    'btw': 'by the way',
    'yoy': 'year over year',
    'fyi': 'for your information',
    'wth': 'what the hell?',
    'idk': "i don't know",
}
while True:
    key = input('''Enter your abbreviation, enter "exit" to quit the program: ''').lower()
    if key in v1.keys(): #dung luon v1 or list(v1)
        print('{0}: {1}'.format(key, v1[key]))
    elif key == "exit":
        break
    else:
        choice = input("Not found the key. Do you want to update new key, Y or N? ").upper()
        if choice == "Y":
            new_def = input("New key's def: ")
            v1[key] = new_def
            print("Added.")
            print()
        else:
            print("please try again")

