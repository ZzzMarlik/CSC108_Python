"""Assignment 2: Palindromes"""

def is_palindrome_word(word: str) -> bool:
    """Return True if and only if the parameter is a palindrome.
    The empty string is considered to be a palindrome.

    >>> is_palindrome_word('abcba')
    True
    >>> is_palindrome_word('')
    True
    >>> is_palindrome_word('abc')
    False
    """

    return word == word[::-1]

def is_palindrome_phrase(phrase: str) -> bool:
    """Return True if and only if the parameter is a palindrome,
    independent of letter case and ignorning non-alphabetic characters.

    >>> is_palindrome_phrase("Madam, I'm Adam.")
    True
    >>> is_palindrome_phrase('nurse run.')
    False
    """

    clean_word = ''
    for s in phrase:
        if s.isalpha():
            clean_word += s
    acc = clean_word.lower()
    return is_palindrome_word(acc)

def get_odd_palindrome_at(word: str, index: int) -> str:
    """Return the longest odd-length palindrome in the string
    that is centered at the specified index.

    >>> get_odd_palindrome_at('aba', 1)
    'aba'
    >>> get_odd_palindrome_at('abcdcab', 3)
    'cdc'
    >>> get_odd_palindrome_at('aab', -1)
    'b'
    """
    center = word[index]
    i = 1
    while index - i >= 0 and index + i < len(word):
        if word[index - i] == word[index + i]:
            center = word[index - i] + center + word[index + i]
        else:
            return center
        i += 1
    return center

if __name__ == '__main__':
    import doctest
    doctest.testmod()
