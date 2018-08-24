# in ra so thich cua minh, moi mot so thich 1 dong
fav_items = ["netflix", 'quora', 'medium']
fav_new =  input("enter what is your fav? ")
fav_items.append(fav_new)
fav_size = len(fav_items)

#1 co cach 1 .
for i in range (fav_size):
    print(i+1, ".", fav_items[i])

#2 khonf co cach
for i in range (fav_size):
    print(i+1, end = "")
    print(".", fav_items[i])

#3 khong co cach 2nd solution
for i in range (fav_size):
    print(i+1, ". ", fav_items[i], sep = "")