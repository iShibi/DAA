# Problem Statement: Implement linear search

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


def linear_search(arr, arr_length, key):
    comparisons = 0
    for i in range(arr_length):
        comparisons += 1
        if (key == arr[i]):
            return [True, comparisons]
    return [False, comparisons]


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        arr_length = int(input())
        arr = list(map(int, input().split(' ')))
        key = int(input())
        key_found, comparisons = linear_search(arr, arr_length, key)
        if (key_found):
            print(f"Present {comparisons}")
        else:
            print(f"Not Present {comparisons}")


main()


'''
Output:

Present 6
Present 3
Not Present 6
'''
