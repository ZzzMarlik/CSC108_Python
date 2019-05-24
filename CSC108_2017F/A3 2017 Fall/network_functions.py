""" CSC108 Assignment 3: Social Networks - Starter code """
from typing import List, Tuple, Dict, TextIO

# CONSTANT VARIABLES
TEST_DIC = {'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'],
            'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy']}

TEST_DIC2 = {'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'],
             'Dylan D-Money': ['Haley Gwendolyn Dunphy']}


# Function Begin
def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]], \
                  person_to_networks: Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.

    Docstring examples not given since result depends on input data.
    """
    firstline = 1
    name = ""
    for line in profiles_file:
        new_name = line.replace("\n", "")
        if (firstline):
            index = new_name.index(",")
            last_name = new_name[0:index]
            first_name = new_name[index + 2:]
            name = first_name + " " + last_name
            firstline = 0
        elif (line == '\n'):
            firstline = 1
        elif ("," not in new_name):
            if (name not in person_to_networks):
                person_to_networks.update({name: [new_name]})
            else:
                person_to_networks.get(name).append(new_name)
        else:
            index = new_name.index(",")
            last_name = new_name[0:index]
            first_name = new_name[index + 2:]
            new_name = first_name + " " + last_name
            if (name not in person_to_friends):
                person_to_friends.update({name: [new_name]})
            else:
                person_to_friends.get(name).append(new_name)
    for keys in person_to_friends:
        person_to_friends.get(keys).sort()
    for keys in person_to_networks:
        person_to_networks.get(keys).sort()


def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """Return the average number of friends that people who appear as keys in
    the given "person to friends" dictionary have.

    >>> get_average_friend_count(TEST_DIC)
    2.0
    >>> get_average_friend_count(TEST_DIC2)
    1.5
    """
    total = 0
    num = len(person_to_friends)
    if (num == 0):
        return 0.0
    for key in person_to_friends:
        total += len(person_to_friends[key])
    return total / num


def get_families(person_to_friends: Dict[str, \
                                         List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first names" dictionary based on the
    given "person to friends" dictionary.

    >>> get_families({})
    {}
    >>> get_families(TEST_DIC2)
    {'Dunphy': ['Haley Gwendolyn'], 'D-Money': ['Dylan'], 'D-Cat': ['Gilbert']}
    """

    dic = {}
    for key in person_to_friends:  # See names in keys
        last_name = (key.split())[-1]  # Get last name
        first_name = (key.split())[:-1]  # Get first name(s)
        temp = ''
        for item in first_name:
            temp = temp + item + ' '
        temp = temp.strip()
        if not last_name in dic:
            dic[last_name] = [temp]
        else:
            if temp not in dic[last_name]:
                dic[last_name].append(temp)
        for value in person_to_friends[key]:  # See names in values
            last = (value.split())[-1]  # Get last/first name same as above
            first = (value.split())[:-1]
            temp = ''
            for item in first:
                temp = temp + item + ' '
            temp = temp.strip()
            if not last in dic:
                dic[last] = [temp]
            else:
                if temp not in dic[last]:
                    dic[last].append(temp)
    for key in dic:
        dic[key].sort()
    return dic


def invert_network(person_to_networks: Dict[str, \
                                            List[str]]) -> Dict[str, List[str]]:
    """Return a "network to people" dictionary based on the given "person to
    networks" dictionary.
    >>> invert_network({})
    {}
    >>> invert_network({'Zy': ['web1', 'web2'], 'Yan': ['web1']})
    {'web1': ['Yan', 'Zy'], 'web2': ['Zy']}
    """

    ret_dict = {}
    for key in person_to_networks:
        for value in person_to_networks[key]:
            if (value not in ret_dict):
                ret_dict[value] = [key]
            else:
                ret_dict[value].append(key)
    for keys in ret_dict:
        ret_dict.get(keys).sort()
    return ret_dict


def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
                           person: str) -> List[str]:
    """Return the list of names of people who are friends of the named person's
    friends.

    >>> get_friends_of_friends(TEST_DIC, 'Haley Gwendolyn Dunphy')
    ['Chairman D-Cat']
    >>> get_friends_of_friends(TEST_DIC, '')
    []
    """
    if person not in person_to_friends:
        return []
    acc = []
    for friend in person_to_friends[person]:
        if friend in person_to_friends:
            for new_friend in person_to_friends[friend]:
                if new_friend != person:
                    acc.append(new_friend)
    acc.sort()
    return acc


def make_recommendations(person: str, person_to_friends: Dict[str, List[str]],
                         person_to_networks: Dict[str, List[str]]) \
    -> List[Tuple[str, int]]:
    """Return the friend recommendations for the given person as a list of
    tuples where the first element of each tuple is a potential friend's name
    (in the same format as the dictionary keys) and the second element is that
    potential friend's score.


    """
    ff_lst = get_friends_of_friends(person_to_friends, person)
    dic = {}
    if person in person_to_friends:  # calculate mutual friend score
        for item in ff_lst:
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
    ret_list = []
    for key, value in dic.items():  # sort
        index = 0
        for tuple in ret_list:
            if (tuple[1] > value):
                index += 1
            elif (tuple[1] == value):
                if (tuple[0] < key):
                    index += 1
        ret_list.insert(index, (key, value))
    return ret_list


if __name__ == '__main__':
    import doctest

    doctest.testmod()
