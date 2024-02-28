from time import sleep, time
import random
from threading import Thread 

def counter(id):
    for i in range(5):
        print("id", id, " value", i)
        sleep(random.randint(2, 6))

start = time()
threads = []
for k in range(4):
    th = Thread(target=counter, args=(k,))
    threads.append(th)
    th.start()
for th in threads:
    th.join()
end = time()
print(end-start)
print("DONE")
