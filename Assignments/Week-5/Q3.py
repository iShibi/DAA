# Problem: You have been given two unsorted integer arrays of size m and n.
# Design an algorithm and implement it using a program to find list of
# elements which are common to both.

'''
Input:

7
34 76 10 39 85 10 55
12
30 55 34 72 10 34 10 89 11 30 69 51
'''

def binary_search(arr, arr_size, key):
    left = 0
    right = arr_size - 1
    while (left <= right):
        mid = left + ((right - left) // 2)
        if (key == arr[mid]):
            return True
        elif (key < arr[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return False

def main():
    M = int(input())
    arr_M = list(map(int, input().split(' ')))
    arr_M.sort()
    N = int(input())
    arr_N = list(map(int, input().split(' ')))
    arr_N.sort()
    res_arr = []
    for el in arr_M:
        if (binary_search(arr_N, N, el)):
            res_arr.append(el)
    print(*res_arr, sep=' ')

main()

'''
Output:

10 10 34 55
'''