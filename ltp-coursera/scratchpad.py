'''
Created on 11/11/2012

@author: repli
'''
import tkinter.filedialog

cat_file = open('cat.txt', mode='r')
cat_string = cat_file.read()

def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def mystery(s):
    ''' (str) -> bool
    '''
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            matches = matches + 1

    return matches == (len(s) // 2)



def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the right
    and shift the last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]

    L[0] = last_item
    
L = ['supu', 'la calva', 'toloco']
    
shift_right(L)

print(L)

def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list
    
    Return a new list in which each item is a 2-item list with the string from the
    corresponding position of list1 and the int from the corresponding position of list2.
    
    Precondition: len(list1) == len(list2)
    
    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''
    
    pairs = []
    
    for i in range(len(list1)):
        pairs.append([list1[i], list2[i]])
        
    return pairs



print(make_pairs(['A', 'B', 'C'], [1, 2, 3]))

def contains(value, lst):
    ''' (object, list of list) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    '''

    found = False  # We have not yet found value in the list.

    # CODE MISSING HERE

    return found

