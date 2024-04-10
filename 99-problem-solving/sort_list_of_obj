

class Test:
    def __init__(self, value, d) -> None:
        self.distance = d
        self.value = value

    def __str__(self) -> str:
        return "[" + self.value + ": " + str(self.distance) + "]"
    

data = []
data.append(Test('A', 67))
data.append(Test('B', 34))
data.append(Test('C', 12))
data.append(Test('D', 67))
data.append(Test('E', 45))
data.append(Test('F', 13))

data.sort(key=lambda x : x.distance)

for t in data:
    print(t)

data[4].distance = 1

data.sort(key=lambda x : x.distance)
print("======")
for t in data:
    print(t)