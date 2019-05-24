"""Types and test data for use in CSC108 Assignment 3"""

from typing import Dict, List, Set

# The IATA code -> list of airport info for that airport.
AirportDict = Dict[str, List[str]]

# The source IATA airport code -> the set of reachable destination IATA
# airport codes.
RouteDict = Dict[str, Set[str]]

# Index information for airport data.
AIRPORT_DATA_INDEXES = {
    'Airport ID': 0,
    'Name': 1,
    'City': 2,
    'Country': 3,
    'IATA': 4,
    'ICAO': 5,
    'Latitude': 6,
    'Longitude': 7,
    'Altitude': 8,
    'Timezone': 9,
    'DST': 10,
    'Tz': 11,
    'Type': 12,
    'Source': 13
}

# Index information for route data.
ROUTE_DATA_INDEXES = {
    'Airline': 0,
    'Airline ID': 1,
    'Source airport': 2,
    'Source airport ID': 3,
    'Destination airport': 4,
    'Destination airport ID': 5,
    'Codeshare': 6,
    'Stops': 7,
    'Equipment': 8
}

"""Test data for use in the doctests in flight_reader and flight_functions
"""

# 5 airports in 5 different countries. A StringIO object can use this as an
# input source for purposes of testing.
TEST_AIRPORTS_SRC = \
    '''1,"Apt1","Cty1","Cntry1","AA1","AAA1",-1,1,1,1,"1","D1","Typ1","Src1"
2,"Apt2","Cty2","Cntry2","AA2","AAA2",-2,2,2,2,"2","D2","Type2","Src2"
3,"Apt3","Cty3","Cntry3","AA3","AAA3",-3,3,3,3,"3","D3","Type3","Src3"
4,"Apt4","Cty4","Cntry4","AA4","AAA4",-4,4,4,4,"4","D4","Type4","Src4"
5,"Apt5","Cty5","Cntry5","\\N","AAA5",-5,5,5,5,"5","D5","Type5","Src5"'''

# Airport information for the airports in TEST_AIRPORTS_SRC.
TEST_AIRPORTS_DICT = {
    'AA1': ['1', 'Apt1', 'Cty1', 'Cntry1', 'AA1', 'AAA1', '-1', '1', '1', '1', '1', 'D1', 'Typ1', 'Src1'],
    'AA2': ['2', 'Apt2', 'Cty2', 'Cntry2', 'AA2', 'AAA2', '-2', '2', '2', '2', '2', 'D2', 'Type2', 'Src2'],
    'AA3': ['3', 'Apt3', 'Cty3', 'Cntry3', 'AA3', 'AAA3', '-3', '3', '3', '3', '3', 'D3', 'Type3', 'Src3'],
    'AA4': ['4', 'Apt4', 'Cty4', 'Cntry4', 'AA4', 'AAA4', '-4', '4', '4', '4', '4', 'D4', 'Type4', 'Src4']
    }

# Routes between the tests airports. A StringIO object can use this as an
# input source for purposes of testing.
# The graph is: 1->2, 2->3, 3->4, 4->1, 1->4, and 3->1
TEST_ROUTES_SRC = \
    '''A1,1111,AA1,1,AA2,2,,0,EQ1
A2,2222,AA2,2,AA3,3,,0,EQ1
A3,3333,AA3,3,AA4,4,,0,EQ1
A4,4444,AA4,4,AA1,1,,0,EQ1
A1,1111,AA1,1,AA4,4,,0,EQ1
A3,3333,AA3,3,AA1,1,,0,EQ1
'''

# The flight routes for the routes in TEST_ROUTES_SRC.
TEST_ROUTES_DICT_FOUR_CITIES = {
    'AA1': {'AA2', 'AA4'},
    'AA2': {'AA3'},
    'AA3': {'AA4', 'AA1'},
    'AA4': {'AA1'}}
