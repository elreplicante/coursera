def is_palindrome_v3(s):
    """(str) -> bool

    Return True if and only if s is a palindrome.
    >>> is_palindrome(noon)
    True
    >>> is_palindrome(racecar)
    True
    >>> is_palindrome(dented)
    False
    """
    i = 0
    j = len(s) - 1
    
    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1
        
    return j <= i
    
def reverse(s):
    """
    
    Returns a reversed version of s
    
    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """
    
    reversed = ''
    for character in s:
        reversed = character + reversed
    
    return reversed

print is_palindrome_v2('hello')