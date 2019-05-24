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
    # define variables
    index = 0
    list_mention = []
    # loop each character of string in order to check the mention
    while index < len(text):
        # check if the character is mention symbol and constrains
        if text[index] == MENTION_SYMBOL and (index == 0 or text[index - 1] == " "):
            mention = first_alnum_substring(text[index + 1:])
            if mention != "":
                list_mention.append(mention)
                index += len(mention)
        index += 1
    return list_mention


# TODO: Add the remaining Assignment 3 functions below.
def extract_hashtags(text: str) -> List[str]:
    """Return a list of all hashtags in text, converted to lowercase, with
    no duplicates included.

    >>> extract_hashtags('Hi @UofT do you like @cats @CATS #meowmeow')
    ['meowmeow']
    >>> extract_hashtags('#cats are #cute #CAts @cat meow @meow')
    ['cats', 'cute']
    >>> extract_hashtags('#many #cats$extra #meow?!')
    ['many', 'cats', 'meow']
    >>> extract_hashtags('No valid mentions #! here?')
    []
    >>> extract_hashtags('No valid mentions #! #here#here?')
    ['here']
    """
    # define variables
    index = 0
    result = []
    # loop each character by counting the index of string to check the tag
    while index < len(text):
        # check if the character is tag symbol
        # and check if the mention symbol is at the begin of tweete of after a space
        if text[index] == HASH_SYMBOL and (index == 0 or text[index - 1] == " "):
            # find the tag words by using helper function
            hashtag = first_alnum_substring(text[index + 1:])
            # check if the hashtag is valid
            if len(hashtag) != 0:
                index += len(hashtag)
                # check if the hashtag is duplicates
                if hashtag not in result:
                    result.append(hashtag)
        index += 1
    return result


def count_words(text: str, words_dic: Dict[str, int]) -> None:
    """No return, update the counts of words in the dictionary

    >>> words_dic = {}
    >>> count_words('#many #cats$extra #meow?!', words_dic)
    >>> words_dic == {'extra': 1}
    True
    >>> count_words('#many #cats$extra #meow?!', words_dic)
    >>> words_dic == {'extra': 2}
    True
    >>> count_words('#many #cats$extra #meow?! http://uoft.com', words_dic)
    >>> words_dic == {'extra': 3}
    True
    >>> words_dic = {}
    >>> count_words('#many #cats @extra #meow?! http://uoft.com', words_dic)
    >>> words_dic == {}
    True
    """
    # split the string into list by whitespace
    text_list = text.split()
    # loop each word in the list
    for word in text_list:
        count_word = ""
        url = True
        # check if the word is mention or hashtag
        if len(word) > 4:
            if word[0:4] == URL_START:
                url = False
        if (word[0] == HASH_SYMBOL or word[0] == MENTION_SYMBOL) and url:
            lower_word = first_alnum_substring(word[1:])
            if len(word[1:]) != len(lower_word):
                count_word = clean_word(word[len(lower_word) + 1:])
        # otherwise, clean the symbol
        elif (word[0] != HASH_SYMBOL and word[0] != MENTION_SYMBOL) and url:
            count_word = clean_word(word)
        
        # check if the count_word is valid
        if len(count_word) != 0:
            # update the dictionary
            if count_word in words_dic:
                words_dic[count_word] += 1
            else:
                words_dic[count_word] = 1


def common_words(words_dic: Dict[str, int], n: int) -> None:
    """
    Return a dictionary containing lowercase words as keys and integer counts
    as values.
    The length of dictionary <= n
    
    >>> words_dic = {"hello":3, "word": 4, "hi":3, "hey": 1}
    >>> common_words(words_dic, 2)
    >>> words_dic == {"word": 4}
    True

    >>> words_dic = {"hello":3, "word": 4, "hi":3, "hey": 1}
    >>> common_words(words_dic, 3)
    >>> words_dic == {"hello":3, "word": 4, "hi":3}
    True

    >>> words_dic = {"hello":3, "word": 4, "hi":3, "hey": 1}
    >>> common_words(words_dic, 1)
    >>> words_dic == {"word": 4}
    True
    
    >>> words_dic = {"hello":3, "word": 4, "hi":3, "hey": 3}
    >>> common_words(words_dic, 2)
    >>> words_dic == {"word": 4}
    True
    """
    # state the new variable
    frequency_dic = {}
    frequency_list = []
    # loop each word in the dictionary
    # reverse the position of key and value
    for word in words_dic:
        frequency = words_dic[word]
        if frequency in frequency_dic:
            frequency_dic[frequency].append(word)
        else:
            frequency_dic[frequency] = [word]
            frequency_list.append(frequency)
    # initialize the new dictionary
    new_words_dic = {}
    # sort the frequency_list from largest number to small number
    frequency_list.sort(reverse=True)
    count = 0
    freq = 0
    # loop each frequency
    while freq < len(frequency_list):
        # get number of words with that frequency
        num_top = len(frequency_dic[frequency_list[freq]])
        # check if the tie words out of n
        if count + num_top <= n:
            # add correspoding word with the frequency into the new dictionary
            for word in frequency_dic[frequency_list[freq]]:
                new_words_dic[word] = words_dic[word]
            count = count + num_top
        # set the freq to the length of frequency_list in order to quit while
        else:
            freq = len(frequency_list)
        freq += 1
    # delete the key from the dictionary
    del_key = []
    for key in words_dic:
        if key not in new_words_dic:
            del_key.append(key)
    for key in del_key:
        del words_dic[key]


def read_tweets(open_file: TextIO) -> Dict[str, List[tuple]]:
    """
    Return a dictionary containing lowercase of username as keys and
    a list of tuples which have the form:
    (tweet text, date, source, favourite count, retweet count)
    as values. 
    
    """
    # add each line into a list
    lines = open_file.read().splitlines()
    # initialize variable
    index = 0
    result = {}
    # check if index is greater then the length of list(lines)
    while index < len(lines):
        # check if it is the username
        if lines[index][-1] == ":":
            user = lines[index][0:-1]
            result[user] = []
            index += 1
        # find the index who indicates the next record or user
        next_record = lines[index:].index("<<<EOT")
        # sublit the record details lines by each property
        details = lines[index].split(",")
        space = " "
        # find the content
        content = space.join(lines[index + 1: next_record + index])
        # add to corresponding postion of list
        result[user].append((content, int(details[FILE_DATE_INDEX]),\
                             details[FILE_SOURCE_INDEX], \
                             int(details[FILE_FAVOURITE_INDEX]),\
                             int(details[FILE_RETWEET_INDEX])))
        index = next_record + index + 1
    return result


def most_popular(user_dict: Dict[str, List[tuple]], date1: int, date2: int) -> str:
    """
    Return the username of the most popular Twitter between the
    time period of date1 and date2 where date1 is less than or equal
    to date2 popularity is the sum of the favourite couns and retweet counts of
    all tweets in that time period

    In case of tie or no tweets, return 'tie'
    
    >>> result = {'UofTCompSci': [('#UofT Prof @ArvindUofT co-authors a report \
    on retraining mid-career workers for #tech https://t.co/L80Ch8FUQb \
    (via @ConversationCA)', 20180928220512, 'Hootsuite Inc.', 1, 4), \
    ('Psst... did you know that you can pair your studies in #compsci \
    with just about any other discipline in @UofTArtSci?  \
    https://t.co/7yEzsGo26R', 20181020151013, 'Hootsuite Inc.', 0, 0)], \
    'UofTArtSci': [('Are @Uber and public transit friends or foes? It \
    depends on the size of city, #UofT study finds     \
    https://t.co/hjG2vooQoE', 20181026184500, 'TweetDeck', 0, 0)]}
    >>> most_popular(result, 20180928220512, 20180928220512)
    'UofTCompSci'
    
    >>> most_popular(result, 20181026184500, 20181026184500)
    'UofTArtSci'
    
    >>> most_popular(result, 20181029184500, 20181029184500)
    'tie'
    
    >>> most_popular(result, 20181020151013, 20181026184500)
    'tie'
    
    >>> most_popular(result, 20180928220512, 20181026184500)
    'UofTCompSci'
    """
    # initialize variables
    user_popular = {}
    list_count = []
    during_period = False
    # loop the use in the user_dict dictionary
    for user in user_dict:
        popular = 0
        # loop each record details tuple
        for record_tuple in user_dict[user]:
            # check if the date is with the period
            if date1 <= record_tuple[TWEET_DATE_INDEX] <= date2:
                popular = popular + record_tuple[TWEET_FAVOURITE_INDEX]\
                    + record_tuple[TWEET_RETWEET_INDEX]
                during_period = True
        # check if the poplular is it and if the date is in period
        if popular in user_popular and during_period:
            user_popular[popular].append(user)
        elif during_period:
            user_popular[popular] = [user]
            list_count.append(popular)
        during_period = False
    # check if it is the case tie(no popular)
    if len(user_popular) == 0:
        return 'tie'
    else:
        max_popular = max(list_count)
        popular_users = user_popular[max_popular]
        # check if it is the case tie(more then one user)
        if len(popular_users) > 1:
            return 'tie'
        else:
            return popular_users[0]
    

def detect_author(user_dict: Dict[str, List[tuple]], tweet: str) -> str:
    """
    Return the username of the most likely author of that tweet, based
    on the hashtags they use.
    If all the hashtags in the tweet are uniquely used by one user, then return
    the username of that author
    Otherwise, return 'unknown'

    
    >>> d = {"a": [("#a #b", 20181108132750, "x", 5, 5)], \
    "b": [("#d", 20181108132751, "y", 5, 5)]}
    >>> detect_author(d, '#a #b abcde')
    'a'
    >>> d = {"u1": [("#a #b", 20181108132750, 'Unknown Location', 1, 1)], \
    "u2": [("#d #b", 20181108132751, "Unknown Location", 1, 1)]}
    >>> detect_author(d, '#a #b abcde')
    'unknown'
    """
    # find the list of hashtags used in tweet
    tweet_hashtags = extract_hashtags(tweet)
    # find a dictionary of hashtags corresponding to list of used username
    users_hashtags = find_all_tags(user_dict)
    # # find a dictionary of a hashtag corresponding to number of people used
    # hashtags_used = find_num_user(users_hashtags)
    
    user_used = []
    # loop each hashtag in tweet_hashtags
    for hashtag in tweet_hashtags:
        # check if hashtag is in users_hashtags dictionary
        if hashtag in users_hashtags:
            # check the length of users
            # case1: muti users use the same tag
            if len(users_hashtags[hashtag]) > 1:
                return 'unknown'
            # case2: only one user use the tag
            if len(users_hashtags[hashtag]) == 1:
                # check if only one user use the single tag
                if users_hashtags[hashtag][0] not in user_used:
                    user_used.append(users_hashtags[hashtag][0])
                if len(user_used) > 1:
                    return 'unknown'
    # check if only one user use the single tag
    if len(user_used) == 1:
        return user_used[0]
    else:
        return 'unknown'


def find_all_tags(user_dict: Dict[str, List[tuple]]) -> Dict[str, List[str]]:
    """
    Return a dictionary containing lowercase of hashtags as keys and
    a list of lowercase of username
    
    This is the helper function to find all hashtags with corresponding list of
    usernames who has used that hashtag
    """
    # initialize variable
    result = {}
    # loop each user in dict
    for user in user_dict:
        # loop each record detail from the dic[user]
        for record in user_dict[user]:
            # get hash
            hashtags = extract_hashtags(record[0])
            # check if the hash tag in return dic and add into user and hash tag into dic
            for hashtag in hashtags:
                if hashtag in result and user not in result[hashtag]:
                    result[hashtag].append(user)
                else:
                    result[hashtag] = [user]
    return result


if __name__ == '__main__':
    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    import doctest
    doctest.testmod()
