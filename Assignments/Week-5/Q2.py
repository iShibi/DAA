# Problem: Given an unsorted array of integers, design an algorithm and implement it using a program
# to find whether two elements exist such that their sum is equal to the given key element.

'''
Input:

2
10
64 28 97 40 12 72 84 24 38 10
50
15
56 10 72 91 29 3 41 45 61 20 11 39 9 12 94
302
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
    test_casees = int(input())
    for _ in range(test_casees):
        arr_size = int(input())
        arr = list(map(int, input().split(' ')))
        arr.sort()
        sum = int(input())
        for num in arr:
            found_keys_flag = False
            key = sum - num
            key_found = binary_search(arr, arr_size, key)
            if (key_found):
                print(f'{num} {key}')
                found_keys_flag = True
                break
        if (found_keys_flag == False):
            print('No Such Elements Exist')
            
main()

'''
Output:

10 40
No Such Elements Exist
'''
