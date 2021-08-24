# Problem: Given an unsorted array of alphabets containing duplicate elements.
# Design an algorithm and implement it using a program to find which alphabet
# has maximum number of occurrences and print it.

'''
Input:

3
10
a e d w a d q a f p
15	
r k p g v y u m q a d j c z e	
20	
g t l l t c w a w g l c w d s a a v c l
'''

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        arr_size = int(input())
        arr = list(map(str, input().split(' ')))
        alphabets_dic = {}
        for letter in arr:
            if (letter in alphabets_dic):
                alphabets_dic[letter] += 1
            else:
                alphabets_dic[letter] = 1
        sorted_alphabets_dic = sorted(alphabets_dic.items(), key = lambda x: x[1], reverse = True)
        [letter, occurence] = sorted_alphabets_dic[0]
        if (occurence <= 1):
            print('No Duplicates Present')
        else:
            print(f'{letter} - {occurence}')

main()

'''
Output:

a - 3
No Duplicates Present
l - 4
'''
