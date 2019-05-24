"""Assignment 3: Tweet Analysis"""

from typing import List, Dict, TextIO, Tuple

HASH_SYMBOL = '#'
MENTION_SYMBOL = '@'
URL_START = 'http'

# Order of data in the file
FILE_DATE_INDEX = 0
FILE_LOCATION_INDEX = 1
FILE_SOURCE_INDEX = 2
FILE_FAVOURITE_INDEX = 3
FILE_RETWEET_INDEX = 4

# Order of data in a tweet tuple
TWEET_TEXT_INDEX = 0
TWEET_DATE_INDEX = 1
TWEET_SOURCE_INDEX = 2
TWEET_FAVOURITE_INDEX = 3
TWEET_RETWEET_INDEX = 4

# Helper functions.

def first_alnum_substring(text: str) -> str:
    """Return all alphanumeric characters in text from the beginning up to the
    first non-alphanumeric character, or, if text does not contain any
    non-alphanumeric characters, up to the end of text."

    >>> first_alnum_substring('')
    ''
    >>> first_alnum_substring('IamIamIam')
    'iamiamiam'
    >>> first_alnum_substring('IamIamIam!!')
    'iamiamiam'
    >>> first_alnum_substring('IamIamIam!!andMore')
    'iamiamiam'
    >>> first_alnum_substring('$$$money')
    ''
    """

    index = 0
    while index < len(text) and text[index].isalnum():
        index += 1
    return text[:index].lower()


def clean_word(word: str) -> str:
    """Return all alphanumeric characters from word, in the same order as
    they appear in word, converted to lowercase.

    >>> clean_word('')
    ''
    >>> clean_word('AlreadyClean?')
    'alreadyclean'
    >>> clean_word('very123mes$_sy?')
    'very123messy'
    """

    cleaned_word = ''
    for char in word.lower():
        if char.isalnum():
            cleaned_word = cleaned_word + char
    return cleaned_word


# Required functions

def extract_mentions(text: str) -> List[str]:
    """Return a list of all mentions in text, converted to lowercase, with
    duplicates included.

    >>> extract_mentions('Hi @UofT do you like @cats @CATS #meowmeow')
    ['uoft', 'cats', 'cats']
    >>> extract_mentions('@cats are #cute @cats @cat meow @meow')
    ['cats', 'cats', 'cat', 'meow']
    >>> extract_mentions('@many @cats$extra @meow?!')
    ['many', 'cats', 'meow']
    >>> extract_mentions('No valid mentions @! here?')
    []
    """
    i = 0
    acc = []
    while text.find(MENTION_SYMBOL, i) != -1:
        hash_index = text.find(MENTION_SYMBOL, i)
        temp = ""
        temp_index = hash_index + 1
        while temp_index < len(text) and text[temp_index].isalpha(): #index out of range
            temp += text[temp_index].lower() # lower case
            temp_index += 1
        if temp != "": # no valid word
            acc.append(temp)
        i = temp_index
    return acc

def extract_hashtags(text: str) -> List[str]:
    """Return a list of all hashtags in text, converted to lowercase, without
    duplicates included.

    >>> extract_hashtags('Hi @UofT do you like @cats @CATS #meowmeow')
    ['meowmeow']
    >>> extract_hashtags('#cats #CATs #cat!!!')
    ['cats', 'cat']
    >>> extract_hashtags('No valid mentions #! here?')
    []
    """
    i = 0
    acc = []
    while text.find(HASH_SYMBOL, i) != -1:
        hash_index = text.find(HASH_SYMBOL, i)
        temp = ""
        temp_index = hash_index + 1
        while temp_index < len(text) and text[temp_index].isalpha(): #index out of range
            temp += text[temp_index].lower() # lower case
            temp_index += 1
        if temp != "" and temp not in acc: # no valid word
            acc.append(temp)
        i = temp_index
    return acc

def count_words(tweet: str, d: Dict[str, int]) -> None:
    """Update the counts of words in the dictionary.
    If a word is not the dictionary yet, it should be added.
    
    >>> d1 = {}
    >>> count_words("#UofT Nick Frosst: Google Brain re-searcher by day, singer @goodkidband by night!", d1)
    >>> d1 == {'nick': 1, 'frosst': 1, 'google': 1, 'brain': 1, 'researcher': 1, 'by': 2, 'day': 1, 'singer': 1, 'night': 1}
    True
    >>> d2 = {"csc108": 1}
    >>> count_words("I love CSC108!  http:Please give me 100 m!a#r$k~", d2)
    >>> d2 == {'csc108': 2, 'i': 1, 'love': 1, 'give': 1, 'me': 1, '100': 1, 'mark': 1}
    True
    """
    lst = tweet.split()
    for item in lst:
        if (item[0].isalpha() or item[0].isdigit()) and item[:4] != URL_START: # TODO
            clean = clean_word(item)
            if clean not in d:
                d[clean] = 1
            else:
                d[clean] += 1

def common_words(d: Dict[str, int], n: int) -> None:
    """update the given dictionary so that it only includes the most common
    words (i.e., the words that appear with the highest frequency).
    At most N words should be kept in the dictionary.
    If including all words with a particular word count would result in a
    dictionary with more than N words, then none of the words with that word
    count should be included.
    
    >>> d1 = {}
    >>> common_words(d1, 3)
    >>> d1 == {}
    True
    >>> d2 = {"csc108": 3, "is": 2, "so": 2, "good": 1}
    >>> common_words(d2, 2)
    >>> d2 == {"csc108": 3}
    True
    """
    invert = {}
    for k, v in d.items():
        invert[v] = invert.get(v, [])
        invert[v].append(k)
    lst = []
    for key in invert:
        lst.append(key)
    lst.sort()
    lst = lst[::-1]
    acc = []
    flag = True
    for item in lst:
        if len(acc) + len(invert[item]) <= n and flag:
            for x in invert[item]:
                acc.append(x)
        else:
            flag = False
    bad = []
    for key in d:
        if key not in acc:
            bad.append(key)
    for key in bad:
        d.pop(key)

def read_tweets(f: (TextIO)) -> Dict[str, List[tuple]]:
    """read all of the data from the given file into a dictionary.
    The keys of the dictionary should be Twitter usernames converted to
    lowercase, and the items in the list associated with each username
    are tuples representing the tweets that user has sent.
    """
    d = {}
    line = f.readline().strip()
    while line:
        if line[-1] == ":":
            name = line[:-1].lower() # lowercase
        d[name] = []
        line = f.readline().strip()
        while line != "" and line[-1] != ":":
            info = line.split(",")
            date = int(info[FILE_DATE_INDEX])
            source = info[FILE_SOURCE_INDEX]
            favour = int(info[FILE_FAVOURITE_INDEX])
            retweet = int(info[FILE_RETWEET_INDEX])
            text = ''
            line = f.readline()
            while line.strip() != '<<<EOT':
                text += line
                line = f.readline()
            tup = (text.strip(), date, source, favour, retweet)
            d[name].append(tup)
            line = f.readline().strip()
    return d

def most_popular(d: Dict[str, List[tuple]], start: int, end: int) -> str:
    """Return the username of the Twitter user who was most popular on Twitter
    between the two dates (inclusive of the start and end dates).
    >>> d1 = {"a": [("hi", 20180101, "x", 5, 5),("hello", 20170101, "x", 1, 0)], "b": [], "c": [("super", 20181111, "y", 11, 0)]}
    >>> most_popular(d1, 20180101, 20190101)
    'c'
    >>> most_popular(d1, 20190101, 20190102)
    'tie'
    >>> most_popular(d1, 20170101, 20190102)
    'tie'
    """
    lst = []
    for key in d:
        score = 0
        for tweet in d[key]:
            if start <= tweet[TWEET_DATE_INDEX] <= end:
                score += tweet[TWEET_FAVOURITE_INDEX]
                score += tweet[TWEET_RETWEET_INDEX]
        if score != 0:
            lst.append((score, key))
    lst.sort()
    if len(lst) == 0 or lst[-1][0] == lst[-2][0]:
        return 'tie'
    else:
        return lst[-1][1]

def detect_author(d: Dict[str, List[tuple]], tweet: str) -> str:
    """Return the username (in lowercase) of the most likely author of that
    tweet, based on the hashtags they use.
    
    >>> d1 = {"a": [("#a", 20180101, "x", 5, 5),("#c", 20170101, "x", 1, 0)], "b": [], "c": [("#c", 20181111, "y", 11, 0)]}
    >>> detect_author(d1, "hi #a")
    'a'
    >>> detect_author(d1, "hi #a #c")
    'unknown'
    >>> detect_author(d1, "hi #b")
    'unknown'
    """
    hash_d = {}
    hash_used = extract_hashtags(tweet)
    for key in d:
        total_text = ""
        for t in d[key]:
            total_text += t[TWEET_TEXT_INDEX]
        temp = extract_hashtags(total_text)
        hash_d[key] = temp
    num = 0
    answer = 'unknown'
    check = True
    for key in hash_d:
        acc = 0
        for item in hash_used:
            if item in hash_d[key]:
                if check:
                    acc += 1
                else:
                    return 'unknown'
        if acc == len(hash_used):
            check = False
            num += 1
            answer = key
    if num == 1:
        return answer
    return 'unknown'
            
if __name__ == '__main__':
    import doctest
    doctest.testmod()