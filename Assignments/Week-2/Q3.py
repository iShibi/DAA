# Problem: Given an array of nonnegative integers, design an algorithm and a program to count the 
# number of pairs of integers such that their difference is equal to a given key, K 

'''
Input:

2
5
1 51 84 21 31
20
10
24 71 16 92 12 28 48 14 20 22
4
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

def pair_counter(arr, arr_size, difference):
    count = 0
    for i in range(arr_size):
        key = arr[i] + difference
        key_found = binary_search(arr, arr_size, key)
        if (key_found):
            count += 1
    return count

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        arr_size = int(input())
        arr = list(map(int, input().split(' ')))
        arr.sort()
        difference = int(input())
        count = pair_counter(arr, arr_size, difference)
        print(f'{count}')

main()

'''
Output:

2
4
'''