"""Starter code for CSC108 Assignment 3"""

from typing import Dict, List, Set, Tuple
from flight_reader import AirportDict, RouteDict, AIRPORT_DATA_INDEXES

def get_airport_info(airports: AirportDict, iata: str, info: str) -> str:
    """Return the airport information for airport with IATA code iata for
    column info from AIRPORT_DATA_INDEXES.

    >>> get_airport_info(TEST_AIRPORTS_DICT, 'AA1', 'Name')
    'Apt1'
    >>> get_airport_info(TEST_AIRPORTS_DICT, 'AA4', 'IATA')
    'AA4'
    """
    return airports[iata][AIRPORT_DATA_INDEXES[info]]

def is_direct_flight(iata_src: str, iata_dst: str, routes: RouteDict) -> bool:
    """Return whether there is a direct flight from the iata_src airport to
    the iata_dst airport in the routes dictionary. iata_src may not
    be a key in the routes dictionary.

    >>> is_direct_flight('AA1', 'AA2', TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_direct_flight('AA2', 'AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    False
    """
    if iata_src in routes:
        return iata_dst in routes[iata_src]
    else:
        return False

def is_valid_flight_sequence(iata_list: List[str], routes: RouteDict) -> bool:
    """Return whether there are flights from iata_list[i] to iata_list[i + 1]
    for all valid values of i. IATA entries may not appear anywhere in routes.

    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2'], TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2', 'AA1', 'AA2'], TEST_ROUTES_DICT_FOUR_CITIES)
    False
    """
    if len(iata_list) == 0:
        return False
    if len(iata_list) == 1:
        return iata_list[0] in routes
    i = 0
    while i < len(iata_list) - 1:
        cur = iata_list[i]
        check = iata_list[i + 1]
        if cur not in routes or (not is_direct_flight(cur, check, routes)):
            return False
        i += 1
    return True

def count_outgoing_flights(iata: str, routes: RouteDict) -> int:
    """Return the number of outgoing flights for the airport with
    the IATA code in the given route information.

    >>> count_outgoing_flights("AA1", TEST_ROUTES_DICT_FOUR_CITIES)
    2
    >>> count_outgoing_flights("BB1", TEST_ROUTES_DICT_FOUR_CITIES)
    0
    """
    if iata in routes:
        return len(routes[iata])
    else:
        return 0

def count_incoming_flights(iata: str, routes: RouteDict) -> int:
    """Return the number of incoming flights for the airport with
    the IATA code in the given route information.

    >>> count_incoming_flights("AA3", TEST_ROUTES_DICT_FOUR_CITIES)
    1
    >>> count_incoming_flights("BB1", TEST_ROUTES_DICT_FOUR_CITIES)
    0
    """
    acc = 0
    for key in routes:
        if iata in routes[key]:
            acc += 1
    return acc

def reachable_destinations(iata: str, limit: int, routes: RouteDict) -> List[Set[str]]:
    """Return a list of the sets of IATA codes reachable from the
    first parameter in steps from 0 up to (and including)
    the maximum number of hops.
    >>> d1 = {'AA1': {'AA2', 'AA4'}, 'AA2': {'AA3'}, 'AA3': {'AA4', 'AA1'}, 'AA4': {'AA1'}}
    >>> ex = [{'AA1'}, {'AA2', 'AA4'}, {'AA3'}]
    >>> reachable_destinations('AA1', 2, d1) == ex
    True
    >>> reachable_destinations('AA1', 0, d1)
    [{'AA1'}]
    """
    reachable_list = [{iata}]
    i = 1
    while i <= limit:
        cur_airports = reachable_list[i - 1]
        new_airports = set()
        for item in cur_airports:
            if item in routes:
                for airport in routes[item]:
                    new_airports.add(airport)
        for s in reachable_list[0:i-1]:
            new_airports = new_airports - s
        reachable_list.append(new_airports)
        i += 1
    return reachable_list

def reverse_dic(d: dict) -> dict:
    """Return a reversed dictionary
    
    >>> reverse_dic({"a":1})
    {1: ['a']}
    >>> reverse_dic({})
    {}
    """
    answer = {}
    for k, v in d.items():
        answer[v] = answer.get(v, [])
        answer[v].append(k)
    return answer

def get_all_distinct(d: dict) -> set:
    """Return a set contains all distinct keys and values in d
    
    >>> get_all_distinct({"a": {"a"}})
    {'a'}
    >>> expected = {1, 'a'}
    >>> get_all_distinct({"a": {1}}) == expected
    True
    """
    total = set()
    for key in d:
        total.add(key)
        for value in d[key]:
            total.add(value)
    return total

def find_busiest_airports(routes: RouteDict, limit: int) -> List:
    """Return the n busiest airports in terms of air traffic volume.
    
    >>> d1 = {'AA1': {'AA2', 'AA4'}, 'AA2': {'AA3'}, 'AA3': {'AA4', 'AA1'}, 'AA4': {'AA1'}}
    >>> find_busiest_airports(d1, 3)
    [('AA1', 4), ('AA3', 3), ('AA4', 3)]
    >>> find_busiest_airports(d1, 2)
    [('AA1', 4)]
    """
    total = get_all_distinct(routes)
    d = {}
    for airport in total:
        d[airport] = count_outgoing_flights(airport, routes) +\
            count_incoming_flights(airport, routes)
    reverse = reverse_dic(d)
    traffic_volume = list(reverse.keys())
    traffic_volume.sort(reverse=True)
    answer = []
    flag = True
    while len(answer) < limit and flag:
        cur_num = traffic_volume[0]
        airports = reverse[traffic_volume.pop(0)]
        airports.sort()
        if len(airports) + len(answer) <= limit:
            for item in airports:
                answer.append((item, cur_num))
        else:
            flag = False
    return answer

if __name__ == '__main__':
    """Uncommment the following as needed to run your doctests"""
    from flight_types_constants_and_test_data import TEST_AIRPORTS_DICT
    from flight_types_constants_and_test_data import TEST_AIRPORTS_SRC
    from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
    from flight_types_constants_and_test_data import TEST_ROUTES_SRC

    import doctest
    doctest.testmod()
