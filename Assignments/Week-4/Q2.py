# Problem: Given an unsorted array of integers, design an algorithm and implement it using a program to sort
# an array of elements by partitioning the array  into  two subarrays based on a pivot  element such
# that one of the sub array holds values smaller than the pivot element while another sub  array holds
# values greater than the pivot element. Pivot element should be selected randomly from the array.
# Your program should also find number of comparisons and swaps required for sorting the array.

'''
Input:

3
8
23 65 21 76 46 89 45 32
10
54 65 34 76 78 97 46 32 51 21
15
63 42 223 645 652 31 324 22 553 12 54 65 86 46 325
'''

def quick_sort(arr, start, end):
    if (start >= end): return
    partition_index = partition(arr, start, end)
    quick_sort(arr, start, partition_index-1)
    quick_sort(arr, partition_index+1, end)

def partition(arr, start, end):
    pivot = arr[end]
    partition_index = start
    for i in range(start, end):
        if (arr[i] <= pivot):
            arr[partition_index], arr[i] = arr[i], arr[partition_index]
            partition_index += 1
    arr[partition_index], arr[end] = arr[end], arr[partition_index]
    return partition_index

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        arr_size = int(input())
        arr = list(map(int, input().split(' ')))
        quick_sort(arr, 0, arr_size-1)
        print(arr)

main()

'''
Output:

[21, 23, 32, 45, 46, 65, 76, 89]
[21, 32, 34, 46, 51, 54, 65, 76, 78, 97]
[12, 22, 31, 42, 46, 54, 63, 65, 86, 223, 324, 325, 553, 645, 652]
'''
