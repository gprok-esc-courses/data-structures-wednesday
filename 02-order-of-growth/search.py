
data = [89, 45, 12, 29, 65, 2, 14, 1]


for i in range(len(data)-1, -1, -1):
    for j in range(i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print(data)