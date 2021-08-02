# Problem: Given  an  unsorted  array  of  integers,  design  an  algorithm  and  implement  a  program  to  sort  this array using selection sort.
# Your program should also find number of comparisons and swaps required.

'''
Input:

3
8
-13 65 -21 76 46 89 45 12
10
54 65 34 76 78 97 46 32 51 21
15
63 42 223 645 652 31 324 22 553 12 54 65 86 46 325
'''

def selection_sort(arr, arr_size):
    swaps = 0
    comparisons = 0
    for i in range(arr_size):
        min_idx = i
        for j in range(i+1, arr_size):
            if arr[min_idx] > arr[j]:
                min_idx = j
            comparisons += 1

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    return [swaps, comparisons]

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        arr_size = int(input())
        arr = list(map(int, input().split(' ')))
        [swaps, comparisons] = selection_sort(arr, arr_size)
        print(f'{arr}\ncomparisons = {comparisons}\nswaps = {swaps}')

main()

'''
Output:

[-21, -13, 12, 45, 46, 65, 76, 89]
comparisons = 28
swaps = 8
[21, 32, 34, 46, 51, 54, 65, 76, 78, 97]
comparisons = 45
swaps = 10
[12, 22, 31, 42, 46, 54, 63, 65, 86, 223, 324, 325, 553, 645, 652]
comparisons = 105
swaps = 15
'''