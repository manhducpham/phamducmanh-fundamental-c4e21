# person = ['Quan', 20, 'Ha Noi', 'Thang Long', 3, 'Da Nang']
# print(person)
#data khong tot, nguoi doc nhin du lieu khong biet co du lieu gi => list thuong dung de bieu dien mot loai du lieu => dictionary bieu dien tot hon.
#dictionary nhieu thong tin nen thuong enter xuong dong.

### empty dictionary
# person = {

# }
# print(person)

### dictionary chua 1 thong tin => gom 2 thu: key va value, ben trai la key, ben phai la value, cach nhau boi colon o giua (web thi dung JSON giong voi dictionary)
# person = {
#     'name': 'Quan'
# }
# print(person)

### generalized dictionary
# person = {
#     'name': 'Quan',
#     'age': 20,
#     'city': 'Hanoi',
# }
# print(person)
# print(person['city'])
# person['city'] = "Da nang"
# print(person)
# key = 'city'
# print(person[key])
# chieu doc (R) thi khong co key se co loi keyerror
# chieu ghi (C or U)
# chieu xoa
person = {
    'name': 'Quan',
    'age': 20,
    'city': 'Hanoi',
}
# print(person['status'])
# person['status'] = 'complicated'
# print(person)
# del person['age']
# print(person)

# for debugging purpose, usually use the k varialbe
for x in person:
    print(x)
for v in person.values():
    print(v)
for k, v in person.items():
    print(k,": ", v, sep = "")
