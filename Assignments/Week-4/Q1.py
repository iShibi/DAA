# Problem: Given an unsorted array of integers, design an algorithm and implement it using a program to sort
# an array of elements by dividing the array into two subarrays and combining these subarrays after
# sorting each one of them. Your program should also find number of comparisons and inversions
# during sorting the array.

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

def merge_sort(arr):
    arr_size = len(arr)
    if (arr_size == 1): return
    mid = arr_size // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    merge_sort(left_arr)
    merge_sort(right_arr)
    merge(left_arr, right_arr, arr)

def merge(left_arr, right_arr, arr):
    i = j = k = 0
    while (i < len(left_arr) and j < len(right_arr)):
        if (left_arr[i] < right_arr[j]):
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while (i < len(left_arr)):
        arr[k] = left_arr[i]
        k += 1
        i += 1
    while (j < len(right_arr)):
        arr[k] = right_arr[j]
        k += 1
        j += 1


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        arr_size = int(input())
        arr = list(map(int, input().split(' ')))
        merge_sort(arr)
        print(arr)

main()

'''
Output:

[21, 23, 32, 45, 46, 65, 76, 89]
[21, 32, 34, 46, 51, 54, 65, 76, 78, 97]
[12, 22, 31, 42, 46, 54, 63, 65, 86, 223, 324, 325, 553, 645, 652]
'''
