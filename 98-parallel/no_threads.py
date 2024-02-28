from time import sleep, time
import random

def counter(id):
    for i in range(5):
        print("id", id, " value", i)
        sleep(random.randint(2, 6))


start = time()
for k in range(4):
    counter(k)
end = time()

print(end-start)