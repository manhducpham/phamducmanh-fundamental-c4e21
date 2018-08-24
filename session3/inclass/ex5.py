fav_items = ['death note', 'netflix', 'teaching']
fav_size = len(fav_items)

print("*" * 20)
for i in range(fav_size):
    print(i + 1, ". ", fav_items[i], sep = "")
print("*" * 20)

# 2nd solution
# for index, item in enumerate(fav_items):
#     print(index + 1, ". ", item, sep = "")

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