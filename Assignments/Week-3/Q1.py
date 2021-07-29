# Problem: Given  an  unsorted  array  of  integers,  design  an  algorithm  and  a  program  to  sort  the  array  using insertion sort.
# Your program should be able to find number of comparisons and shifts required for sorting the array.

'''
Input:

3
8
-23 65 -31 76 46 89 45 32
10
54 65 34 76 78 97 46 32 51 21
15
63 42 223 645 652 31 324 22 553 -12 54 65 86 46 325
'''

def insertion_sort(arr, arr_size):
    shifts = 0
    comparisons = 0
    for i in range(1, arr_size):
        current = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > current):
            comparisons += 1
            arr[j+1] = arr[j]
            shifts += 1
            j -= 1
        arr[j+1] = current
        shifts += 1
    return [shifts, comparisons]

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        arr_size = int(input())
        arr = list(map(int, input().split(' ')))
        # the function sorts the array in-place and returns the count of shifts and comparisons that were done
        [shifts, comparisons] = insertion_sort(arr, arr_size)
        print(f'{arr}\ncomparisons = {comparisons}\nshifts = {shifts}')

main()

'''
Output:

[-31, -23, 32, 45, 46, 65, 76, 89]
comparisons = 13 
shifts = 20 
[21, 32, 34, 46, 51, 54, 65, 76, 78, 97]7 
comparisons = 28 
shifts = 37 
[-12, 22, 31, 42, 46, 54, 63, 65, 86, 223, 324, 325, 553, 645, 652]
comparisons = 54
shifts = 68 
'''