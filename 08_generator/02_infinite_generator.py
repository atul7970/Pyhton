def infinite_counter():
    """A generator that yields an infinite sequence of integers, starting from 1."""
    n = 1
    while True:
        yield n
        n += 1

counter = infinite_counter()

for _ in range(10):  # Print the first 10 numbers from the infinite counter
    print(next(counter))    