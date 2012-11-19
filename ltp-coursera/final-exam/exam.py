'''
Created on 18/11/2012

@author: repli
'''


def f(x):
    y = x * 3
    return y - x

def swap_words(two_words):
    '''(str) -> str

    Precondition: two_words is a string containing two words separated by one space.

    Return a new string where the words are in reverse order, again separated by
    one space.

    >>> swap_word('Hello World')
    World Hello
    '''

    first = two_words[:two_words.find(' ')]
    second = two_words[two_words.find(' ') + 1:]
    print(second + ' ' + first)


swap_words('Hello World')


def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int

    s1 and s2 are strings, and letter is a string of length 1.  Count how many
    times letter appears in s1 and in s2, and return the bigger of the two
    counts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''

    return max(s1.count(letter), s2.count(letter))

print(count_max_letters('hello', 'world', 'l'))
print(count_max_letters('cat', 'abracadabra', 'a'))

def both_start_with(s1, s2, prefix):
    '''(str, str, str) -> bool

    Return True if and only if s1 and s2 both start with the letters in prefix.
    '''
    return s1.startswith(prefix) and s2.startswith(prefix)

print(both_start_with('america', 'españa', 'a'))

print(both_start_with('america', 'angola', 'a'))

def reverse(s):
    '''(str) -> str

    Return the reverse of s.

    >>> reverse('abc')
    'cba'
    >>> reverse('a')
    'a'
    >>> reverse('madam')
    'madam'
    >>> reverse('1234!')
    '!4321'
    '''

    result = ''
    i = len(s) - 1
    while i >= 0:
        result = result + s[i]
        i = i - 1

    return result

print(reverse('abc'))

def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    ['a', 1]
    '''

    result = []
    for k in d:
        if k in L:
            result.append(k)

    return result

print(get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'}))


def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool

    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''

    result = True
    for i in range(len(L1)):
        if L1[i] != len(L2[i]):
            result = False

    return result

print(are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef']))

def double_values(collection):
    for v in range(len(collection)):
        collection[v] = collection[v] * 2
        
d = {0: 10, 1: 20, 2: 30}
double_values(d)


def get_negative_nonnegative_lists(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            val = L[row][col]
            if val < 0:
                neg.append(val)
            else:
                nonneg.append(val)

    return (neg, nonneg)


print(get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]]))