def is_palindrome(str):
    '''(str) -> bool

    Pre-condition: str consisting only of lowercase alphabetic letters

    Return True iff the str is palindrome

    >>>is_palindrome('radar')
    True
    >>>is_palindrome('toots')
    False
    '''

    return str == str[::-1]

def is_palindromic_phrase(phrase):
    '''(str) -> bool

    Return True iff the phrase is palidromic

    >>>is_palindromic_phrase("Madam, I'm Adam.")
    True
    >>>is_palindromic_phrase('nurse run.')
    False
    '''

    acc = ''
    for i in phrase:
        if i.isalpha():
            acc += i
    return is_palindrome(acc.lower())

def get_odd_palindrome_at(letters, location):
    '''(str, int) -> str

    Pre-conditon: letters only consist lowercase alphabetic characters and
    location must be the valid index into the letters.

    Return the longest odd-length palindrome in the letters that is centered at
    the specified location.

    >>>get_odd_palindrome_at('abcba', 2)
    'abcba'
    >>>get_odd_palindrome_at('abcdcab', 3)
    'cdc'
    >>>get_odd_palindrome_at('abcdcbaf', 3)
    'abcdcba'
    >>>get_odd_palindrome_at('hefgfeh', -4)
    'hefgfeh'
    '''
    acc = letters[location]
    i = 1
    if location < 0:
        location = location + len(letters)
    while 0 <= location - i and location + i + 1 <= len(letters):
        if is_palindrome(letters[location - i:location + i + 1]):
            acc = letters[location - i:location + i + 1]
            i += 1
        else:
            return acc
    return acc
