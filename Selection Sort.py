# For selection sort,
# the space complexity in the worst-case scenario
# is O(1),
# the time complexity is O(n^2)
# an iterative approach has been taken
# to implement the algorithm
# the minimum index shall  be updated
# with every iteration

def selectionSort(array, num):
    min_idx = 0
    for i in range(0, num):
        min_idx = i
        for j in range(i+1, num):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

a = [10, 1, 3, 7, 5]
n = len(a)
print(a)
selectionSort(a, n)
print(a)
