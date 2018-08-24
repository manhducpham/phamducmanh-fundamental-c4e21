# 1. tao ra list liet ke 2 - 3 thu moi nguoi thich
# 2. hoi user 1 so thich moi
# 3. them so thich moi vao danh sach khai bao
# 4. in lai

favorite_items = ['gym', "swimming", "chatting"]
print(*favorite_items, sep = ", ")

new_favorite = input("What is your favorite activities? ")
favorite_items.append(new_favorite)
print(*favorite_items, sep = ", ")