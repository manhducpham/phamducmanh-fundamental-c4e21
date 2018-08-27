prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

for k in prices.keys():
    print(k.capitalize())
    print('Price:', prices[k])
    print('Stock:', stock[k])
    print()

total = 0
for k in prices.keys():
    price = float(prices[k])
    number = float(stock[k])
    value = price * number
    total += value
    print("The value of {0} in stock is:".format(k), value)
print("Total value of the stock is:", total)