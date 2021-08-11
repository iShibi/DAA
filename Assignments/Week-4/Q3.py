# Problem: Given an unsorted array of integers, design an algorithm and implement it using a
# program to find Kth smallest or largest element in the array.

'''
Input:

2
10
123 656 54 765 344 514 765 34 765 234
3
15
43 64 13 78 864 346 786 456 21 19 8 434 76 270 601
8
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
        k = int(input())
        quick_sort(arr, 0, arr_size-1)
        if (k > arr_size):
            print("Not Present")
        else:
            print(arr[k-1])

main()

'''
Output:

123
78
'''
