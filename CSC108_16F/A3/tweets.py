def extract_mentions(tweet):
    '''(str) -> list of str

    Return a list containing all of the mentions in the tweet, in the order
    they appear in the tweet.

    >>> extract_mentions('Hello #csc108')
    []
    >>> extract_mentions('Hello @Mark123 @Eve123')
    ['Mark123', 'Eve123']
    >>> extract_mentions('Repeat @Mark,@Mark')
    ['Mark']
    '''

    lst = tweet.split()
    acc = []
    result = []
    for i in lst:
        if i[0] == '@':
            acc.append(i)
    for item in acc:
        result.append(get_alnum(item[1:]))
    return result

def extract_hashtags(tweet):
    '''(str) -> list of str

    return a list containing all of the hashtags in the tweet,
    in the order they appear in the tweet.

    >>> extract_hashtags('Hello @csc108')
    []
    >>> extract_hashtags('Hello #Mark123 #Eve123')
    ['Mark123', 'Eve123']
    >>> extract_hashtags('Repeat #Mark, #Mark')
    ['Mark']
    '''
    lst = tweet.split()
    acc = []
    result = []
    answer = []
    for i in lst:
        if i[0] == '#':
            acc.append(i)
    for item in acc:
        result.append(get_alnum(item[1:]))
    for s in result:
        if s not in answer:
            answer.append(s)
    return answer

def count_words(tweet, dic):
    '''(str, dict of {str: int}) -> None

    Update the counts of words of the tweet in the dictionary.

    >>> tweet = 'Hello? how are you you you'
    >>> dic = {'hello': 1, 'how': 1, 'you': 1}
    >>> count_words(tweet, dic)
    >>> dic
    {'hello': 2, 'are': 1, 'you': 4, 'how': 2}

    >>> tweet = 'HAVE A NICE DAY! @TA #csc108 https://t.co/x62lrGm1MB'
    >>> dic = {}
    >>> count_words(tweet, dic)
    >>> dic
    {'nice': 1, 'a': 1, 'day': 1, 'have': 1}
    '''

    lst = tweet.split()
    lst2 = []
    lst3 = []
    for i in lst:
        if i[0] != '@' and i[0] != '#' and i[:4] != 'http':
            lst2.append(i)
    for i in lst2:
        words = ''
        for item in i:
            if item.isalnum():
                words += item
            i = words.lower()
        lst3.append(i)
    for str in lst3:
        if str in dic:
            dic[str] += 1
        else:
            dic[str] = 1

def common_words(dic: Dict[str, int], N: int) -> None:
    '''(dict of {str: int}, int) -> None

    Update the dictionary so that it includes the most common
    (highest frequency words). At most N words should be included in the
    dictionary.

    >>> dic = {'Kevin': 100, 'Eve': 120, 'Tiffany': 99}
    >>> common_words(dic, 1)
    >>> dic
    {'Eve': 120}

    >>> dic = {'Kevin': 130, 'Eve': 120, 'Tiffany': 120}
    >>> common_words(dic, 2)
    >>> dic
    {'Kevin': 130}
    '''

    name_lst = extract_lst(sort_dic(dic, N))
    acc = []
    for key in dic:
        if key not in name_lst:
            acc.append(key)
    for item in acc:
        dic.pop(item)

def read_tweets(file):
    '''(file open for reading) -> dict of {str: list of tweet tuples}

    Return a dictionary that formed by the file and it contains the details of
    tweets that every candidates sent

    '''
    dic = {}
    line = file.readline()
    while line != '':
        if line[-2:-1] == ':':
            name = line[:-2]
        line = file.readline()
        tweet = []
        while line != '' and line[-2:-1] != ':':
            lst = line.strip().split(',')
            line = file.readline()
            text = ''
            while line.strip('\n') != '<<<EOT':
                text += line
                line = file.readline()
            tweet.append((name, text, int(lst[1]), lst[3], int(lst[-2]),
                          int(lst[-1])))
            line = file.readline()
        dic[name] = tweet
    return dic

def most_popular(dic, start, finish):
    '''(dict of {str: list of tweet tuples}, int, int) -> str

    Return which candidate was the most popular on Twitter between
    start date and finish date (inclusive of the start and end dates) based on
    their tweet dic.

    >>> most_popular({'Mark': [('Mark', 'Hi', 2016, 'Iphone', 100, 200),
    ('Mark', 'Hi', 2017, 'Iphone', 100, 200)],
    'Eve': [('Eve', 'Hi', 2016, 'Iphone', 50, 200)]}, 2015, 2016)
    'Mark'
    >>> most_popular({'Mark': [('Mark', 'Hi', 2016, 'Iphone', 100, 200),
    ('Mark', 'Hi', 2017, 'Iphone', 100, 200)],
    'Eve': [('Eve', 'Hi', 2016, 'Iphone', 100, 200)]}, 2015, 2016)
    "Tie"
    '''

    d = {}
    for i in dic:
        like = 0
        for item in dic[i]:
            if start <= item[2] <= finish:
                like += item[4] + item[5]
            d[i] = like
    if len(sort_dic(d, 1)) == 0:
        return "Tie"
    else:
        return extract_lst(sort_dic(d, 1))[0]

def detect_author(dic, tweet):
    '''(dict of {str: list of tweet tuples}, str) -> str

    Return the username of the most likely author of that tweet,
    based on the hashtags they use from the given dic.

    >>> detect_author({'k': [('k', '#Hi', 2016, 'Iphone', 100, 200),
    ('k', '#Hii', 2017, 'Iphone', 100, 200)],
    'e': [('e', '#Hi', 2016, 'Iphone', 100, 200)]}, '#Hii')
    'k'
    >>> detect_author({'k': [('k', '#Hi', 2016, 'Iphone', 100, 200),
    ('k', '#Hii', 2017, 'Iphone', 100, 200)],
    'e': [('e', '#Hi', 2016, 'Iphone', 100, 200)]}, '#Hi')
    'Unknown'
    '''

    d = count_tags(dic)
    d2 = get_unique_key(str_exchange(d))
    tweet_tag = extract_hashtags(tweet)
    lst1 = []
    acc = []
    for i in tweet_tag:
        if i in d2:
            lst1.append(d2[i])
    lst2 = extract_lst(lst1)
    if len(lst2) == 0:
        return 'Unknown'
    s = 0
    while s < len(lst2) - 1 and len(lst2) > 1:
        if lst2[s] != lst2[s+1]:
            return 'Unknown'
        s += 1
    return lst2[0]

# --- Helper Functions ---

def exchange(dic):
    '''(dict of {str: int}) -> dict of {int: list of str}

    Return the new dictionary from the dic that exchange the position
    of keys and values.

    >>> exchange({'Mark': 130, 'Eve': 120, 'Tiffany': 120})
    {120: ['Eve', 'Tiffany'], 130: ['Mark']}
    >>> exchange({})
    {}
    '''

    keys = []
    values = []
    for item in dic:
        keys.append(item)
    for s in dic:
        values.append(dic[s])
    new_keys = []
    for a in keys:
        new_keys.append([a])
    d = {}
    i = 0
    while i < len(values):
        if values[i] in d:
            d[values[i]].extend(new_keys[i])
        else:
            d[values[i]] = (new_keys[i])
        i += 1
    return d

def sort_dic(dic, N):
    '''(dict of {str: int}, int) -> list of lists of str

    Return the list so that it includes the most common
    (highest frequency words) in the dic. At most N words should be
    included in the list.

    >>> sort_dic({'Mark': 130, 'Eve': 120, 'Tiffany': 120}, 2)
    [['Mark']]
    >>> sort_dic({'Mark': 130, 'Eve': 120, 'Tiffany': 120}, 0)
    []
    '''

    d = exchange(dic)
    lst = []
    for b in d:
        lst.append(b)
    lst.sort()
    lst2 = lst[::-1]
    names = []
    total = 0
    i = 0
    while i < len(lst2) and total <= N:
        names.append(d[lst2[i]])
        total += len(d[lst2[i]])
        if total > N:
            names.pop()
            break
        i += 1
    return names

def extract_lst(lst):
    '''(list of lists of str) -> list

    Return the list contains every element in the lst

    >>> extract_lst([['Mark'], ['Eve', 'Tiffany']])
    ['Mark', 'Eve', 'Tiffany']
    >>> extract_lst([])
    []
    '''

    names = []
    for i in lst:
        for item in i:
            names.append(item)
    return names

def str_exchange(dic):
    '''(dict of {str: list of str}) -> dict of {str: list of str}

    Return the new dictionary from the dic that exchange the position
    of keys and values.

    >>> str_exchange({'Mark': ['Hi', 'Hii'], 'Eve': ['Hi']})
    {'Hii': ['Mark'], 'Hi': ['Eve', 'Mark']}
    >>> str_exchange({})
    {}
    '''

    acc = {}
    for key in dic:
        for value in dic[key]:
            acc[value] = acc.get(value, []) + [key]
    return acc

def count_tags(dic):
    '''(dict of {str: list of str}) -> dict of {str: list of str}

    Return the dictionary that contaions candidates name as keys and all the
    hashtags they said as values from the given dic.

    >>> count_tags({'Mark': [('Mark', 'fff#Hi', 2016, 'Iphone', 100, 200),
    ('Mark', 'fff#Hii', 2017, 'Iphone', 100, 200)],
    'Eve': [('Eve', 'ee#Hi', 2016, 'Iphone', 100, 200)]})
    {'Mark': ['Hi', 'Hii'], 'Eve': ['Hi']}

    >>> count_tags({'Mark': [('Mark', 'fff#Hi', 2016, 'Iphone', 100, 200),
    ('Mark', 'fff#Hii', 2017, 'Iphone', 100, 200)],
    'Eve': [('Eve', 'Hi', 2016, 'Iphone', 100, 200)]})
    {'Mark': ['Hi', 'Hii'], 'Eve': []}
    '''

    d = {}
    for i in dic:
        tags = []
        for item in dic[i]:
            total = ''
            total += item[1]
            if extract_hashtags(total) not in tags:
                tags.append(extract_hashtags(total))
            d[i] = extract_lst(tags)
    return d

def get_alnum(str):
    '''(str) -> str

    Return the str that only contains alnum.

    >>> get_alnum('Hi\n')
    Hi
    >>> get_alnum('')
    ''
    '''
    acc = ''
    for i in str:
        if i.isalnum():
            acc += i
        else:
            return acc
    return acc

def get_unique_key(dic):
    '''(dict of {str: list of str}) -> dict of {str: list of str}

    Return the dictionary that only can contains keys that are only assigned to
    one value.

    >>> get_unique_tag({'x': ['1', '2'], 'y': ['3']})
    {'y': ['3']}
    >>> get_unique_tag({'x': ['1', '2'], 'y': ['3', '4']})
    {}
    '''
    acc = []
    for key in dic:
        if len(dic[key]) > 1:
            acc.append(key)
    for item in acc:
        dic.pop(item)
    return dic
