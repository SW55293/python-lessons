def count_1s(n):
    counter = 0

    while n:
        counter += n % 2
        n = n >> 2
    return counter

print(count_1s(10))