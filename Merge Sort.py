# For merge sort
# the space complexity is O(n)
# while the time complexity of O(n*lgn)

def mergeSort(array, num):
    width = 1
    while width <= num:
        left = 0
        while left <= num:
            right = min(left+(width*2-1), num-1)
            middle = min(left+width, num-1)
            merge(array, left, middle, right)
            left += width*2
        width *= 2

def merge(array, left, middle, right):
    num1 = middle - left + 1
    num2 = right - middle
    leftArray = [0]*num1
    rightArray = [0]*num2
    for i in range(num1):
        leftArray[i] = array[left+i]
    for j in range(num2):
        rightArray[j] = array[middle + j + 1]
    i, j, k = 0, 0, left
    while i < num1 and j < num2:
        if leftArray[i] <= rightArray[i]:
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1
        k += 1
    while i < num1:
        array[k] = leftArray[i]
        i += 1
        k += 1
    while j < num2:
        array[k] = rightArray[j]
        j += 1
        k += 1


a = [10, 1, 3, 7, 5]
n = len(a)
print(a)
mergeSort(a, n)
print(a)
