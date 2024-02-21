
def binary_to_decimal(s: str) -> int:
    exponent = 0
    total = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == '1':
            total += 2 ** exponent
        exponent += 1
    return total

def decimal_to_binary(n: int) -> str:
    pass

print(binary_to_decimal('10101100010'))
