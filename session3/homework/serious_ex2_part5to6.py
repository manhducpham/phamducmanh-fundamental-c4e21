flock_sizes = [5, 7, 300, 90, 24, 50, 75]
flock_num = len(flock_sizes)
print("Hello, my name is Manh and these are my ship sizes: ")
print(flock_sizes)
print()

### 2.5
n = 2 # the time horizon
for i in range(n):
    print("MONTH {0}".format(i + 1))
    monthly_growth = 50
    for ind in range(flock_num):
        flock_sizes[ind] += monthly_growth
    print("One month has passed, now here is my flock:")
    print(flock_sizes)

    max_size = max(flock_sizes)
    print("Now my biggest sheep has size {0} let's shear it!".format(max_size))

    default_size = 8
    max_size_position = flock_sizes.index(max_size)
    flock_sizes[max_size_position] = default_size
    print("After shearing, here is my flock:")
    print(flock_sizes)
    print()

### 2.6
print("MONTH {0}".format(n + 1))
monthly_growth = 50
for ind in range(flock_num):
    flock_sizes[ind] += monthly_growth
print("One month has passed, now here is my flock:")
print(flock_sizes)
print()

total_size = 0
price = 2
for i in range(flock_num):
    total_size += flock_sizes[i]
print("My flock has size in total: {0}".format(total_size))
print("I would get {0} * {1}$ = {2}$".format(total_size, price, total_size * price))