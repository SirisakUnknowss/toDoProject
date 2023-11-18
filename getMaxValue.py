def getMaxValue():
    arr = [1,2,1,3,5,6,4]
    indexMax = 0
    lastValue = arr[0]
    for index, data in enumerate(arr):
        if data > lastValue:
            indexMax = index
            lastValue = data
    return indexMax

print("index max value is " + getMaxValue())