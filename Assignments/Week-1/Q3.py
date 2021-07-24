# Problem Statement: Implement jump search

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

import math


def jump_search(arr, arr_length, key):
    block_size = math.floor(math.sqrt(arr_length))
    left = 0
    right = block_size
    comparisons = 0
    while (right < arr_length and arr[right] <= key):
        comparisons += 1
        left = right
        right += block_size
    for i in range(left, right):
        comparisons += 1
        if (key == arr[i]):
            return [True, comparisons]
    return [False, comparisons]


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        arr_length = int(input())
        arr = list(map(int, input().split(' ')))
        arr.sort()
        key = int(input())
        key_found, comparisons = jump_search(arr, arr_length, key)
        if (key_found):
            print(f"Present {comparisons}")
        else:
            print(f"Not Present {comparisons}")


main()

'''
Output:

Present 5
Present 1
Not Present 3
'''
