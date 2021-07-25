# Problem: Given a sorted array of positive integers, design an algorithm and implement it using a program to 
# find three indices i, j, k such that arr[i] + arr[j] = arr[k]

'''
Input:

3
5
1 5 84 209 341
10  
24 28 48 71 86 89 92 120 194 201  
15  
64 69 82 95 99 107 113 141 171 350 369 400 511 590 666
'''

def find_indices(arr, arr_size):
    for i in range(arr_size):
        for j in range(i+1, arr_size):
            for k in range(j+1, arr_size):
                if (arr[i] + arr[j] == arr[k]):
                    return [i, j, k]
    return None

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        arr_size = int(input())
        arr = list(map(int, input().split(' ')))
        indices = find_indices(arr, arr_size)
        if (indices):
            print(f'{indices[0]}, {indices[1]}, {indices[2]}')
        else:
            print('No sequence found')

main()

'''
Output:

No sequence found
1, 6, 7
0, 5, 8
'''