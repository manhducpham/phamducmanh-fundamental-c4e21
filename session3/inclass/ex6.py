fav_items = ['death note', 'netflix', 'teaching']
fav_size = len(fav_items)

print("*" * 20)
for i in range(fav_size):
    print(i + 1, ". ", fav_items[i], sep = "")
print("*" * 20)

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