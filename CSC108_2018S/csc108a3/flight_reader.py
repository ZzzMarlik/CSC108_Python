"""Functions for CSC108 Assignment 3 to read in the airport and route data.
"""

from typing import TextIO

# Note about "from io import StringIO" in the docstrings:
# We can use StringIO to pretend that a string is the contents of a file.
# We are only using it for the examples below, to help you understand what
# the functions will do. 
# You do NOT have to use it yourself.

from flight_types_constants_and_test_data import AIRPORT_DATA_INDEXES, \
     ROUTE_DATA_INDEXES, AirportDict, RouteDict

def read_airports(airports_source: TextIO) -> AirportDict:
    """Return a dictionary containing the information in airports_source.
    Skip entries that have no IATA code.

    >>> from io import StringIO
    >>> airports_src = StringIO(TEST_AIRPORTS_SRC)
    >>> airports_res = read_airports(airports_src)
    >>> airports_res['AA1'][0], airports_res['AA1'][1]
    ('1', 'Apt1')
    >>> airports_res['AA4'][0], airports_res['AA4'][1]
    ('4', 'Apt4')
    >>> len(airports_res)
    4
    >>> airports_res == TEST_AIRPORTS_DICT
    True
    """
    iata_index = AIRPORT_DATA_INDEXES['IATA']
    d = {}
    line = airports_source.readline()
    while line != '':
        temp = line.strip().split(",")
        i = 0
        while i < len(temp):
            temp[i] = temp[i].strip('"')
            i += 1
        key = temp[iata_index]
        if '\\N' not in key and key != '':
            d[temp[iata_index]] = temp
        line = airports_source.readline()
    return d

def read_routes(routes_source: TextIO, airports: AirportDict) -> RouteDict:
    """Return the flight routes from routes_source, including only the ones
    that have an entry in airports. If there are multiple routes between
    routes_source and a destination (on different airlines for example),
    include the destination only once. Routes that include null airport IDs
    should still be included, but routes that have empty IATA should be
    excluded.

    >>> from io import StringIO
    >>> routes_src = StringIO(TEST_ROUTES_SRC)
    >>> actual = read_routes(routes_src, TEST_AIRPORTS_DICT)
    >>> actual == TEST_ROUTES_DICT_FOUR_CITIES
    True
    """

    routes = {}
    src_index = ROUTE_DATA_INDEXES['Source airport']
    dst_index = ROUTE_DATA_INDEXES['Destination airport']
    lst = []
    for key in airports:
        lst.append(key)
    for line in routes_source.readlines():
        temp = line.strip().split(",")
        if temp[src_index] in lst and temp[dst_index] in lst:
            if temp[src_index] not in routes:
                routes[temp[src_index]] = {temp[dst_index]}
            else:
                routes[temp[src_index]].add(temp[dst_index])
    return routes


if __name__ == '__main__':
    """Uncommment the following as needed to run the doctests"""
    from flight_types_constants_and_test_data import TEST_AIRPORTS_DICT
    from flight_types_constants_and_test_data import TEST_AIRPORTS_SRC
    from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
    from flight_types_constants_and_test_data import TEST_ROUTES_SRC

    import doctest
    doctest.testmod()
