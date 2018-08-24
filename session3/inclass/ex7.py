fav_items = ['death note', 'netflix', 'teaching']
fav_size = len(fav_items)

print("*" * 20)
for i in range(fav_size):
    print(i + 1, ". ", fav_items[i], sep = "")
print("*" * 20)

fav_del = (input("Which item do you want to delete? "))
#1: not check
# fav_items.remove(fav_del)
# fav_size_new = len(fav_items)
# print("*" * 20)
# for i in range(fav_size_new):
#     print(i + 1, ". ", fav_items[i], sep = "")
# print("*" * 20)

#2: check new function
# def check_item(name):
#     flag = False
#     for i in range(fav_size):
#         if name == fav_items[i]:
#             flag = True
#     return flag


# if check_item(fav_del) == True:
#     fav_items.remove(fav_del)
#     fav_size_new = len(fav_items)
#     print("*" * 20)
#     for i in range(fav_size_new):
#         print(i + 1, ". ", fav_items[i], sep = "")
#     print("*" * 20)
# else:
#     print("The item that you want to delete is out of the list. Please check the grammar again.")
#3
if fav_del in fav_items:
    fav_items.remove(fav_del)
    fav_size_new = len(fav_items)
    print("*" * 20)
    for i in range(fav_size_new):
        print(i + 1, ". ", fav_items[i], sep = "")
    print("*" * 20)
else:
    print("The item that you want to delete is out of the list. Please check the grammar again.")
#2: check new function
def check_item(name):
    flag = False
    for i in range(fav_size):
        if name == fav_items[i]:
            flag = True
    return flag

flag = check_item(fav_del)
if flag == True:
    fav_items.remove(fav_del)
    fav_size_new = len(fav_items)
    print("*" * 20)
    for i in range(fav_size_new):
        print(i + 1, ". ", fav_items[i], sep = "")
    print("*" * 20)
else:
    print("The item that you want to delete is out of the list. Please check the grammar again.")