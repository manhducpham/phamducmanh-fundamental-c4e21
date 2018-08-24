# item1 = 'com rang'
# item2 = 'pho bo'
# item3 = 'my xao'
# item4 = 'bun bo'
# item5 = 'bun oc'
# item6 = 'mien tron'
# moi lan them du lieu (add or create)
# tim kiem kho khan

### INITIALIZE
### list variable, use s or list at the end of word
# menu_items = []
# print(menu_items)

### list 1 phan tu
# menu_items = ["com rang"]
# print(menu_items)

### list nhieu phan tu
# menu_items = ["Com rang", "Pho bo"]
# print(menu_items)
# newitem = "Mi xao"
# menu_items.append(newitem)
# print(menu_items)
# # insert
# menu_items.inser
# print(menu_items)

# menu_items = ["Com rang", "Pho bo", "My xao"]
# print(menu_items[0]) #python is zero - based language => bat dau tu 0
# print(menu_items[-1]) #python la ngon ngu cuon nen -1 la phan tu cuoi cung, va chi cuon 1 lan
# print(menu_items[-4]) khong duoc.
# range tu -3 den 2
# print(len(menu_items))
# #thuong luu len duoi dang 1 bien
# menu_size = len(menu_items)
# print(menu_size)
# for item in menu_items:
#     print(item)
# menu_items = ["Com rang", "Pho bo", "My xao"]
# menu_items[1] = "Tai chin" #truy cap duoc thi coi nhu la mot bien
# for index, item in enumerate(menu_items):
#     print(index + 1, item)

# delete
menu_items = ["Com rang", "Pho bo", "My xao", "Mien tron"]
print(menu_items)
menu_items.pop(1)
print(menu_items)
menu_items.remove("My xao")
print(menu_items)