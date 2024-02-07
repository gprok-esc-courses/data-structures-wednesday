from typing import List

# passing by value
def chance_value(x: int) -> None:
    x = x * 2

# passing by reference
def change_list(data: List) -> None:
    for i in range(len(data)):
        data[i] = data[i] * 2

a = 5
chance_value(a)
print(a)

d = [10, 20, 30, 40]
change_list(d)
print(d)
