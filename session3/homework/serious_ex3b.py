from random import randint, choice

words_list = ['champion', 'victory', 'destroy', 'event']
words_num = len(words_list)
n = randint(0, words_num - 1)
word = words_list[n]
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