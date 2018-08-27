letter_count = {}
sentence = input("Enter your sentence: ").lower()
for letter in sentence:
    letter_count[letter] = letter_count.get(letter, 0) + 1
del letter_count[" "]
letter_items = list(letter_count.items())
letter_items.sort()
for i in letter_items:
    print(*i, sep = "\t")