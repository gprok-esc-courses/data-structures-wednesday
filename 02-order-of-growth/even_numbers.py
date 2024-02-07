import random
from time import time

def find_even_numbers(data):
    counter = 0
    for value in data:
        if value % 2 == 0:
            counter += 1
    return counter

values = [100000, 1000000, 10000000, 100000000]

for v in values:
    data = [random.randint(1, 1000) for i in range(v)]
    start_time = time()
    find_even_numbers(data)
    end_time = time()
    print(v, " Elapsed: ", end_time-start_time)