

def hanoi(n, source, destination, helper):
    if n > 0:
        hanoi(n - 1, source, helper, destination)
        print(n, 'from', source, 'to', destination)
        hanoi(n - 1, helper, destination, source)


hanoi(4, 'A', 'C', 'B')