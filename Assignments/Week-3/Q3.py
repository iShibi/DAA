# Problem: Given an unsorted array of positive integers, design an algorithm and implement it using a program 
# to find whether there are any duplicate elements in the array or not.

'''
Input:

3
5
28 52 83 14 75
10
75 65 1 65 2 6 86 2 75 8
15
75 35 86 57 98 23 73 1 64 8 11 90 61 19 20
'''

def insertion_sort(arr, arr_size):
    for i in range(1, arr_size):
        current = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > current):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current

def have_duplicates(arr, arr_aize):
    insertion_sort(arr, arr_aize)
    for i in range(arr_aize-1):
        if (arr[i] == arr[i+1]):
            return True
    return False


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        arr_size = int(input())
        arr = list(map(int, input().split(' ')))
        if(have_duplicates(arr, arr_size)):
            print("Yes")
        else:
            print("No")

main()

'''
Output:

No
Yes
No
'''