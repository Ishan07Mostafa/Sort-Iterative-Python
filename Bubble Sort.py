# For bubble sort,
# the space complexity is O(1)
# while the time complexity
# in the worst-case scenario
# is O(n^2)
# However
# an optimized algorithm will give
# O(n)

def bubbleSort(array, n):
    for i in range(n):
        for j in range(n-i-1):
            if array[j] < array[j+1]:
                continue
            else:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def bubbleSortOptimized(array, n):
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if array[j] < array[j+1]:
                continue
            else:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if swapped == False:
            break




a = [10,1,3,7,5]
b = a
print(a)
print(b)
n = len(a)
bubbleSort(a, n)
bubbleSortOptimized(b,n)
print(a)
print(b)
