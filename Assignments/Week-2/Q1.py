# Problem: Given a sorted array of positive integers containing few duplicate elements, design an algorithm 
# and implement it using a program to find whether the given key element is present in the array or 
# not. If present, then also find the number of copies of given key

'''
Input:

2
10
235 235 278 278 763 764 790 853 981 981
981
15
1 2 2 3 3 5 5 5 25 75 75 75 97 97 97
75
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

def counter(arr, arr_size, key):
    count = 0
    for i in range(arr_size):
        if (key == arr[i]):
            count += 1
        elif (count > 0):
            break
    return count

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        arr_size = int(input())
        arr = list(map(int, input().split(' ')))
        key = int(input())
        key_found = binary_search(arr, arr_size, key)
        if (key_found):
            count = counter(arr, arr_size, key)
            print(f'{key} - {count}')
        else:
            print('Key not present')

main()

'''
Output:

981 - 2
75 - 3
'''