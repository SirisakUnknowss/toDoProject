import math
def getCountZero(factorial):
    value = 1
    for i in range(1, factorial + 1):
        value *= i
    n = 1
    result = 0
    while result == 0:
        result = value % (10 ** n)
        if result != 0:
            break
        n += 1
    countZero = n - 1
    print(f"value is {value}")
    return countZero


count = getCountZero(10)
print(f"zero after value count is {count}")