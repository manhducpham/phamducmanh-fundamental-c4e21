from random import randint, choice

word = "champion"
chars = list(word)
chars_len = len(chars)

for i in range(chars_len):
    t = choice(chars)
    print(t, end = " ")
    chars.remove(t)
print()

guess = input("Enter the word: ").lower()
if  guess == word:
    print("Great, you're amazing!!!")
else:
    print("Wrong, please try again :(")