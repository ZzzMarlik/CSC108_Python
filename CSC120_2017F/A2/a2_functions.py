# Reminders:

# Add descriptions in all functions.
# Add 2 examples in the docstring of all functions except for load_profiles.

# Do not use open, input, print, or close anywhere in your a2_functions.py file.

# Do not use break or continue anywhere in your code. It is OK if you do not know
# what break or continue is :)

# CONSTANT VARAIBLE
FRIEND_TEST= {'Jay Pritchett': ['Gloria Pritchett', 'Manny Delgado', 'Claire Dunphy'],
              'Claire Dunphy': ['Phil Dunphy', 'Mitchell Pritchett', 'Jay Pritchett'],
              'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'],
              'Mitchell Pritchett': ['Claire Dunphy', 'Cameron Tucker', 'Luke Dunphy'],
              'Alex Dunphy': ['Luke Dunphy'],
              'Cameron Tucker': ['Mitchell Pritchett', 'Gloria Pritchett'],
              'Haley Gwendolyn Dunphy': ['Dylan D-Money'],
              'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'],
              'Dylan D-Money': ['Haley Gwendolyn Dunphy'],
              'Gloria Pritchett': ['Jay Pritchett', 'Cameron Tucker', 'Manny Delgado'],
              'Luke Dunphy': ['Manny Delgado', 'Alex Dunphy', 'Phil Dunphy', 'Mitchell Pritchett']}
WEB_TEST = {'Phil Dunphy': ['Real Estate Association'],
            'Claire Dunphy': ['Parent Teacher Association'],
            'Manny Delgado': ['Chess Club'],
            'Mitchell Pritchett': ['Law Association'],
            'Alex Dunphy': ['Orchestra', 'Chess Club'],
            'Cameron Tucker': ['Clown School', 'Wizard of Oz Fan Club'],
            'Gloria Pritchett': ['Parent Teacher Association']}

# Helper Function
def check_same_lst(lst1, lst2):
    """(list of item, list of item) -> Boolean
    
    Return True iff elements in lst1 are same as lst2 without considering order.
    
    >>> check_same_lst([1, 1], [2, 1])
    False
    >>> check_same_lst([1, 2], [2, 1])
    True
    """
    
    if len(lst1) != len(lst2):
        return False
    temp = lst2
    for item in lst1:
        if item not in temp:
            return False
        else:
            temp.remove(item)
    return True

def check_same_dic(dic1, dic2):
    """(dict of {str: list of str}, dict of {str: list of str)}) -> Boolean
    
    Return True iff dic1 is same as dic2 without considering order of keys.
    
    >>> check_same_dic({}, {})
    True
    >>> check_same_dic({'a': [1, 2]}, {'a': [2, 1]})
    True
    """
    
    if len(dic1) != len(dic2):
        return False
    for key in dic1:
        if key not in dic2:
            return Flase
    for key in dic1:
        if not check_same_lst(dic1[key], dic2[key]):
            return Flase
    return True
    
# Required Functions
def load_profiles(profiles_file, person_to_friends, person_to_networks):
    """ (file open for reading, dict of {str: list of str},
         dict of {str: list of str}) -> NoneType

         Update the two dictionaries by adding the data from the open file
         to them.
    """

    # Add your code for this function here.
    line = profiles_file.readline()
    while line != '':
        index = line.find(',')
        name = line.strip()[index + 2:] + ' ' + line.strip()[:index]
        line = profiles_file.readline()
        net = []
        while ',' not in line and line != '': # load network info
            net.append(line.strip())
            line = profiles_file.readline()
        if name not in person_to_networks and net != []: # update network dic
            person_to_networks[name] = net
        else:
            for item in net:
                if item not in person_to_networks[name]:
                    person_to_networks[name].append(item)
        friend = []
        if line != '\n' and line != '':
            while line != '\n' and line != '': # load friend info
                index = line.find(',')
                friend.append(line.strip()[index + 2:] + ' ' + line.strip()[:index])
                line = profiles_file.readline()
        if name not in person_to_friends and friend != []: # update friend dic
            person_to_friends[name] = friend
        else:
            for item in friend:
                if item not in person_to_friends[name]:
                    person_to_friends[name].append(item)
        line = profiles_file.readline()


def invert_networks_dict(person_to_networks):
    """ (dict of {str: list of str}) -> dict of {str: list of str}

    Return a "network to people" dictionary based on the given "person to networks" dictionary.

    >>> acc = invert_networks_dict(WEB_TEST)
    >>> check_same_dic(acc, {'Wizard of Oz Fan Club': ['Cameron Tucker'], 'Real Estate Association': ['Phil Dunphy'], 'Orchestra': ['Alex Dunphy'], 'Clown School': ['Cameron Tucker'], 'Law Association': ['Mitchell Pritchett'], 'Parent Teacher Association': ['Claire Dunphy', 'Gloria Pritchett'], 'Chess Club': ['Manny Delgado', 'Alex Dunphy']})
    True
    >>> invert_networks_dict({})
    {}
    """

    # Add your code for this function here.
    acc = {}
    for key in person_to_networks:
        for value in person_to_networks[key]:
            if (value not in acc):
                acc[value] = [key]
            else:
                acc[value].append(key)
    return acc


def make_recommendations(person, person_to_friends, person_to_networks):
    """ (str, dict of {str: list of str}, dict of {str: list of str})
        -> list of (str, int) tuple

    Return the friend recommendations for the given person in a list of tuples where the first
     element of each tuple is a potential friend's name (in the same format as the dictionary keys)
      and the second element is that potential friend's score.

    >>> result1 = make_recommendations('Jay Pritchett', FRIEND_TEST, WEB_TEST)
    >>> exp1 = [('Mitchell Pritchett', 2), ('Cameron Tucker', 1), ('Luke Dunphy', 1), ('Phil Dunphy', 1)]
    >>> check_same_lst(result1, exp1)
    True
    >>> result2 = make_recommendations('Claire Dunphy', FRIEND_TEST, WEB_TEST)
    >>> exp2 = [('Manny Delgado', 1), ('Cameron Tucker', 1), ('Luke Dunphy', 3), ('Gloria Pritchett', 2)]
    >>> check_same_lst(result2, exp2)
    True
    """

    # Add your code for this function here.
    dic = {}
    acc = []
    if person in person_to_friends: # find mutual friends
        for friend in person_to_friends[person]:
            if friend in person_to_friends:
                for new_friend in person_to_friends[friend]:
                    if new_friend != person:
                        acc.append(new_friend)
    if person in person_to_friends:  # calculate mutual friend score
        for item in acc:
            if item not in person_to_friends[person]:
                if item not in dic:
                    dic[item] = 1
                else:
                    dic[item] += 1
    if person in person_to_networks:  # calculat network socre
        for network in person_to_networks[person]:
            for key in dic:
                if key in person_to_networks and network in person_to_networks[key]:
                    dic[key] += 1
    for key in dic:  # consider same last name
        if key.split()[1] == person.split()[1]:
            dic[key] += 1
    result = []
    for key, value in dic.items():
        result.append((key, value))
    return result

def sort_recommendations(recommendations):
    """ (list of (str, int) tuple) -> list of str

    Return a list of potential friend's names ordered by score (highest to lowest).

    >>> sort_recommendations([('Manny Delgado', 1), ('Cameron Tucker', 1), ('Luke Dunphy', 3), ('Gloria Pritchett', 2)])
    ['Luke Dunphy', 'Gloria Pritchett', 'Cameron Tucker', 'Manny Delgado']
    >>> sort_recommendations([('Mitchell Pritchett', 2), ('Cameron Tucker', 1), ('Luke Dunphy', 1), ('Phil Dunphy', 1)])
    ['Mitchell Pritchett', 'Cameron Tucker', 'Luke Dunphy', 'Phil Dunphy']
    """

    # Add your code for this function here.
    dic = {}
    score_lst = []
    acc = []
    for item in recommendations: # make a dic of {score: names}
        score_lst.append(item[1]) # also save the appearance of socres
        if item[1] not in dic:
            dic[item[1]] = [item[0]]
        else:
            dic[item[1]].append(item[0])
    for key in dic: # sort the names
        dic[key].sort()
    score_lst.sort()
    score_lst = score_lst[::-1] # sort and reverse the socre list
    for i in range(len(score_lst)): # get the sort name list by socres list
        acc.append(dic[score_lst[i]].pop(0))
    return acc