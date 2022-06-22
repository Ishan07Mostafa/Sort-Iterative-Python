# For quick sort
# the space complexity is O(n)
# while the time complexity is O(n*lgn)

def partition(array, low, high):
    i = low - 1
    x = array[high]
    for j in range(low, high):
        if array[j] < x:
            i += 1
            array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
    return i + 1

def quickSort(array, low, high):
    size = high - low + 1
    stack = [0]*size
    top = 0
    stack[top] = low
    top += 1
    stack[top] = high
    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1
        p = partition(array, low, high)
        if p-1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = p - 1
        elif p-1 < high:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = high

a = [10, 1, 3, 7, 5]
n = len(a)
print(a)
quickSort(a, 0, n-1)
print(a)
