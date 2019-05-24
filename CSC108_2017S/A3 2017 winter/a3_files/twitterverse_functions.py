"""
Type descriptions of Twitterverse and Query dictionaries
(for use in docstrings)

Twitterverse dictionary:  dict of {str: dict of {str: object}}
    - each key is a username (a str)
    - each value is a dict of {str: object} with items as follows:
        - key "name", value represents a user's name (a str)
        - key "location", value represents a user's location (a str)
        - key "web", value represents a user's website (a str)
        - key "bio", value represents a user's bio (a str)
        - key "following", value represents all the usernames of users this
          user is following (a list of str)

Query dictionary: dict of {str: dict of {str: object}}
   - key "search", value represents a search specification dictionary
   - key "filter", value represents a filter specification dictionary
   - key "present", value represents a presentation specification dictionary

Search specification dictionary: dict of {str: object}
   - key "username", value represents the username to begin search at (a str)
   - key "operations", value represents the operations to perform (a list of str)

Filter specification dictionary: dict of {str: str}
   - key "following" might exist, value represents a username (a str)
   - key "follower" might exist, value represents a username (a str)
   - key "name-includes" might exist, value represents a str to match (a case-insensitive match)
   - key "location-includes" might exist, value represents a str to match (a case-insensitive match)

Presentation specification dictionary: dict of {str: str}
   - key "sort-by", value represents how to sort results (a str)
   - key "format", value represents how to format results (a str)

"""

# Write your Twitterverse functions here


def process_data(file):
    """ (file open for reading) -> Twitterverse dictionary

    Read the file and return the data in the Twitterverse dictionary format.

    """
    d = {}
    line = file.readline()
    while line != '': # loop until file end
        temp = line.strip()
        d[temp] = {}
        line = file.readline()
        d[temp]['name'] = line.strip() # Add name info
        line = file.readline()
        d[temp]['location'] = line.strip() # Add location info
        line = file.readline()
        d[temp]['web'] = line.strip() # Add web info
        line = file.readline()
        bio = ''
        while line != 'ENDBIO\n': # loop to get all bio info
            bio += line
            line = file.readline()
        d[temp]['bio'] = bio.strip()
        line = file.readline().strip()
        following = []
        while line != 'END': # loop to get all following info
            following.append(line.strip())
            line = file.readline().strip()
        d[temp]['following'] = following
        line = file.readline()
    return d


def process_query(file):
    """(file open for reading) -> query dictionary

    Read the file and return the query in the query dictionary format.

    """
    d = {}
    line = file.readline() # pass unnecessary info
    line = file.readline()
    d['search'] = {} # make a search dic
    d['search']['username'] = line.strip() # Add username
    line = file.readline()
    operation = []
    while line != 'FILTER\n': # loop to get all operation info
        operation.append(line.strip())
        line = file.readline()
    d['search']['operations'] = operation # Add all operations
    d['filter'] = {} # make a filter dic
    line = file.readline()
    while line != 'PRESENT\n': # loop to get all filter info
        d['filter'][line.split()[0]] = line.split()[1] # Add filter method
        line = file.readline()
    line = file.readline()
    d['present'] = {} # make a present dic
    d['present']['sort-by'] = line.split()[1] # Add sort method
    line = file.readline()
    d['present']['format'] = line.split()[1] # Add format method
    return d


def all_followers(dictionary, username):
    """ (Twitterverse dictionary, str) -> list of str

    Identify all the usernames that are following the user
    specified by the second parameter and return them as a list.

    >>> d = {'Sheldon': {'following': ['katieH', 'NicoleKidman']}}
    >>> all_followers(d, 'NicoleKidman')
    ['Sheldon']
    >>> all_followers(d, 'Markk')
    []
    """
    acc = []
    for key in dictionary:
        if username in dictionary[key]['following']:
            acc.append(key)
    return acc


def get_search_results(twitter_dic, search_dic):
    """ (Twitterverse dictionary, search specification dictionary) -> list of str

    Perform the specified search on the given Twitter data, and return a list
    of strings representing usernames that match the search criteria.

    >>> twitter_dic = {'Sheldon': {'following': ['katieH', 'NicoleKidman']}}
    >>> search_dic = {'username': 'Sheldon', 'operations': ['following']}
    >>> get_search_results(twitter_dic, search_dic)
    ['katieH', 'NicoleKidman']
    >>> search_dic = {'username': 'Sheldon', 'operations': ['followers']}
    >>> get_search_results(twitter_dic, search_dic)
    []
    """
    result = [search_dic['username']] # get initial list
    for i in search_dic['operations']:
        acc = []
        if i == 'followers': # case 1: find all followers
            while len(result) > 0:
                temp = all_followers(twitter_dic, result.pop(0))
                for item in temp: # check duplicate
                    if item not in acc:
                        acc.append(item)
            result = acc[:]
        elif i == 'following': # case 2: find all followings
            while len(result) > 0:
                temp = twitter_dic[result.pop(0)]['following']
                for item in temp: # check duplicate
                    if item not in acc:
                        acc.append(item)
            result = acc[:]
    return result


def get_filter_results(twitter_dic, username_list, filter_dic):
    """ (Twitterverse dictionary, list of str, filter specification dictionary) -> list of str

    Apply the specified filters to the given username list to determine which
    usernames to keep, and return the resulting list of usernames.

    >>> twitter_dic = {'Sheldon': {'name': 'Shuai Shao', 'location': 'Canada', 'web': '', 'bio': '', 'following': ['katieH', 'NicoleKidman']}}
    >>> username_list = ['Sheldon']
    >>> filter_dic = {'following': 'katieH'}
    >>> get_filter_results(twitter_dic, username_list, filter_dic)
    ['Sheldon']
    >>> filter_dic = {'following': 'KatieH', 'location-includes': 'USA'}
    >>> get_filter_results(twitter_dic, username_list, filter_dic)
    []
    """
    acc = username_list[:] # avoid modifying the parameters
    for key in filter_dic:
        if key == 'name-includes': # case 1: filter name-includes
            L1 = []
            for i in acc:
                if filter_dic[key].lower() in i.lower():
                    L1.append(i)
            acc = L1 # update the result
        if key == 'location-includes': # case 2: filter location-includes
            L2 = []
            for i in acc:
                if filter_dic[key].lower() in twitter_dic[i]['location'].lower():
                    L2.append(i)
            acc = L2 # update the result
        if key == 'following': # case 3: filter following
            follower_list = all_followers(twitter_dic, filter_dic[key])
            L3 = []
            for i in acc:
                if i in follower_list:
                    L3.append(i)
            acc = L3 # update the result
        if key == 'follower': # case 4: filter follower
            L4 = []
            for i in acc:
                if (filter_dic[key] in twitter_dic[i]['following']):
                    L4.append(i)
            acc = L4 # update the result
    return acc


def get_present_string(twitter_dic, username_list, present_dic):
    """ (Twitterverse dictionary, list of str, presentation specification dictionary) -> str

    Format the results for presentation based on the given presentation
    specification and return the formatted string.

    >>> twitter_dic = {'quietTweeter': {'name': '', 'bio': '', 'location': '', 'web': '', 'following': []}}
    >>> present_dic = {'sort-by': 'username', 'format': 'short'}
    >>> get_present_string(twitter_dic, ['quietTweeter'], present_dic)
    "['quietTweeter']"
    >>> present_dic = {'sort-by': 'username', 'format': 'short'}
    >>> get_present_string(twitter_dic, [], present_dic)
    '[]'
    """
    acc = username_list[:] # avoid modifying the parameters
    if present_dic['sort-by'] == 'popularity': # case 1 for sort method
        tweet_sort(twitter_dic, acc, more_popular)
    elif present_dic['sort-by'] == 'name': # case 2 for sort method
        tweet_sort(twitter_dic, acc, name_first)
    elif present_dic['sort-by'] == 'username': # case 3 for sort method
        tweet_sort(twitter_dic, acc, username_first)
    if present_dic['format'] == 'short': # case 1 for format method
        return str(acc)
    if present_dic['format'] == 'long': # case 2 for format method
        result = ''
        if len(acc) == 0: # special case: when the username list is empty
            result += '----------\n----------'
            return result
        for i in acc: # loop to get all info and form in a long format
            result += '----------\n' + i + '\n'
            result += 'name: ' + twitter_dic[i]['name'] + '\n'
            result += 'location: ' + twitter_dic[i]['location'] + '\n'
            result += 'website: ' + twitter_dic[i]['web'] + '\n'
            result += 'bio:' + '\n' + twitter_dic[i]['bio'] + '\n'
            result += 'following: ' + str(twitter_dic[i]['following']) + '\n'
        result += '----------\n'
        return result


# --- Sorting Helper Functions ---


def tweet_sort(twitter_data, results, cmp):
    """ (Twitterverse dictionary, list of str, function) -> NoneType

    Sort the results list using the comparison function cmp and the data in
    twitter_data.

    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> result_list = ['c', 'a', 'b']
    >>> tweet_sort(twitter_data, result_list, username_first)
    >>> result_list
    ['a', 'b', 'c']
    >>> tweet_sort(twitter_data, result_list, name_first)
    >>> result_list
    ['b', 'a', 'c']
    """

    # Insertion sort
    for i in range(1, len(results)):
        current = results[i]
        position = i
        while position > 0 and cmp(twitter_data, results[position - 1], current) > 0:
            results[position] = results[position - 1]
            position = position - 1
        results[position] = current


def more_popular(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int

    Return -1 if user a has more followers than user b, 1 if fewer followers,
    and the result of sorting by username if they have the same, based on the
    data in twitter_data.

    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> more_popular(twitter_data, 'a', 'b')
    1
    >>> more_popular(twitter_data, 'a', 'c')
    -1
    """

    a_popularity = len(all_followers(twitter_data, a))
    b_popularity = len(all_followers(twitter_data, b))
    if a_popularity > b_popularity:
        return -1
    if a_popularity < b_popularity:
        return 1
    return username_first(twitter_data, a, b)


def username_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int

    Return 1 if user a has a username that comes after user b's username
    alphabetically, -1 if user a's username comes before user b's username,
    and 0 if a tie, based on the data in twitter_data.

    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> username_first(twitter_data, 'c', 'b')
    1
    >>> username_first(twitter_data, 'a', 'b')
    -1
    """

    if a < b:
        return -1
    if a > b:
        return 1
    return 0


def name_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int

    Return 1 if user a's name comes after user b's name alphabetically,
    -1 if user a's name comes before user b's name, and the ordering of their
    usernames if there is a tie, based on the data in twitter_data.

    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> name_first(twitter_data, 'c', 'b')
    1
    >>> name_first(twitter_data, 'b', 'a')
    -1
    """

    a_name = twitter_data[a]["name"]
    b_name = twitter_data[b]["name"]
    if a_name < b_name:
        return -1
    if a_name > b_name:
        return 1
    return username_first(twitter_data, a, b)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
