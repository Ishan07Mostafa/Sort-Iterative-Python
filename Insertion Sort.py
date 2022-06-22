# For insertion sort
# the space complexity is O(1)
# while the time complexity is O(n^2)
# it is a rather simple algorithm

def insertionSort(array, num):
    for i in range(1, num):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key


a = [10, 1, 3, 7, 5]
n = len(a)
print(a)
insertionSort(a, n)
print(a)
