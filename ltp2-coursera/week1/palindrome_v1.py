def is_palindrome_v1(s):
    """(str) -> bool

    Return True if and only if s is a palindrome.
    >>> is_palindrome(noon)
    True
    >>> is_palindrome(racecar)
    True
    >>> is_palindrome(dented)
    False
    """
    
    return reverse(s) == s
    
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

print(is_palindrome_v1('noon'))