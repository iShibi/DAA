# Problem Statement: Implement binary search

'''
Input:

3
8
34 35 65 31 25 89 64 30
89
5
977 354 244 546 355
244
6
23 64 13 67 43 56
63
'''


def binary_search(arr, arr_length, key):
    left = 0
    right = arr_length - 1
    comparisons = 0
    while (left <= right):
        mid = left + ((right - left) // 2)
        if (key == arr[mid]):
            comparisons += 1
            return [True, comparisons]
        elif (key < arr[mid]):
            right = mid - 1
            comparisons += 1
        else:
            left = mid + 1
            comparisons += 1
    return [False, comparisons]


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        arr_length = int(input())
        arr = list(map(int, input().split(' ')))
        arr.sort()
        key = int(input())
        key_found, comparisons = binary_search(arr, arr_length, key)
        if (key_found):
            print(f"Present {comparisons}")
        else:
            print(f"Not Present {comparisons}")


main()

'''
Output:

Present 4
Present 2
Not Present 3
'''
