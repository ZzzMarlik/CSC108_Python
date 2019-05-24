""" CSC108 Assignment 2 Starter code """

from typing import List, TextIO

# A set of constants, each representing a list index for station information.
ID = 0
NAME = 1
LATITUDE = 2
LONGITUDE = 3
CAPACITY = 4
BIKES_AVAILABLE = 5
DOCKS_AVAILABLE = 6
IS_RENTING = 7
IS_RETURNING = 8

####### BEGIN HELPER FUNCTIONS ####################

def is_number(value: str) -> bool:
    """Return True if and only if value represents a decimal number.

    >>> is_number('csc108')
    False
    >>> is_number('  108 ')
    True
    >>> is_number('+3.14159')
    True
    """

    return value.strip().lstrip('-+').replace('.', '', 1).isnumeric()


# It isn't necessary to call this function to implement your bikes.py
# functions, but you can use it to create larger lists for testing.
# See the main block below for an example of how to do that.
def csv_to_list(csv_file: TextIO) -> List[List[str]]:
    """Read and return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of csv_file.

    Docstring examples not given since results depend on data to be input.
    """

    # Read and discard header.
    csv_file.readline()

    data = []
    for line in csv_file:
        data.append(line.strip().split(','))
    return data


####### END HELPER FUNCTIONS ####################

### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####

SAMPLE_STATIONS = [
    [7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False]]

HANDOUT_STATIONS = [
    [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11, True, True],
    [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,
     15, 5, 10, True, True]]

#########################################

def clean_data(data: List[list]) -> None:
    """Convert each string in data to an int if and only if it represents a
    whole number, a float if and only if it represents a number that is not a
    whole number, True if and only if it is 'True', False if and only if it is
    'False', and None if and only if it is either 'null' or the empty string.

    >>> d = [['abc', '123', '45.6', 'True', 'False']]
    >>> clean_data(d)
    >>> d
    [['abc', 123, 45.6, True, False]]
    >>> d = [['ab2'], ['-123'], ['False', '3.2']]
    >>> clean_data(d)
    >>> d
    [['ab2'], [-123], [False, 3.2]]
    """
    j = 0
    while j < len(data):
        i = 0
        while i < len(data[j]):
            if type(data[j][i]) == str and is_number(data[j][i]):
                if "." in data[j][i]:
                    data[j][i] = float(data[j][i])
                else:
                    data[j][i] = int(data[j][i])
            if data[j][i] == "True":
                data[j][i] = True
            if data[j][i] == "False":
                data[j][i] = False
            i += 1
        j += 1


def get_station_info(station_id: int, stations: List[list]) -> list:
    """Return a list containing the following information from stations
    about the station with id number station_id:
        - station name
        - number of bikes available
        - number of docks available
    (in this order)

    Precondition: station_id will appear in stations.

    >>> get_station_info(7087, SAMPLE_STATIONS)
    ['Danforth/Aldridge', 9, 14]
    >>> get_station_info(7088, SAMPLE_STATIONS)
    ['Danforth/Coxwell', 13, 2]
    """
    acc = []
    i = 0
    while i < len(stations):
        if stations[i][ID] == station_id:
            acc.append(stations[i][NAME])
            acc.append(stations[i][BIKES_AVAILABLE])
            acc.append(stations[i][DOCKS_AVAILABLE])
        i += 1
    return acc

def get_total(index: int, stations: List[list]) -> int:
    """Return the sum of the column in stations given by index.

    Precondition: the items in stations at the position
                  that index refers to are ints.

    >>> get_total(BIKES_AVAILABLE, SAMPLE_STATIONS)
    22
    >>> get_total(DOCKS_AVAILABLE, SAMPLE_STATIONS)
    16
    """
    acc = 0
    i = 0
    while i < len(stations):
        acc += stations[i][index]
        i += 1
    return acc

def get_station_with_max_bikes(stations: List[list]) -> int:
    """Return the station ID of the station that has the most bikes available.
    If there is a tie for the most available, return the station ID that appears
    first in stations.

    Precondition: len(stations) > 0

    >>> get_station_with_max_bikes(SAMPLE_STATIONS)
    7088
    """
    i = 0
    acc = 0
    while i < len(stations):
        if stations[i][BIKES_AVAILABLE] > acc:
            acc = stations[i][BIKES_AVAILABLE]
            station_id = stations[i][ID]
        i += 1
    return station_id

def get_stations_with_n_docks(n: int, stations: List[list]) -> List[int]:
    """Return a list containing the station IDs for the stations in stations
    that have at least n docks available, in the same order as they appear
    in stations.

    Precondition: n >= 0

    >>> get_stations_with_n_docks(2, SAMPLE_STATIONS)
    [7087, 7088]
    >>> get_stations_with_n_docks(5, SAMPLE_STATIONS)
    [7087]
    """
    acc = []
    i = 0
    while i < len(stations):
        if stations[i][DOCKS_AVAILABLE] >= n:
            acc.append(stations[i][ID])
        i += 1
    return acc

def get_direction(start_id: int, end_id: int, stations: List[list]) -> str:
    """ Return a string that contains the direction to travel to get from
    station start_id to station end_id according to data in stations.

    Precondition: start_id and end_id will appear in stations.

    >>> get_direction(7087, 7088, SAMPLE_STATIONS)
    'SOUTHWEST'
    """
    acc = ""
    if start_id == end_id:
        return acc
    i = 0
    while i < len(stations):
        if stations[i][ID] == start_id:
            start = stations[i]
        if stations[i][ID] == end_id:
            end = stations[i]
        i += 1
    if end[LONGITUDE] > start[LONGITUDE]:
        acc += "NORTH"
    if end[LONGITUDE] == start[LONGITUDE]:
        acc += ''
    if end[LONGITUDE] < start[LONGITUDE]:
        acc += "SOUTH"
    if end[LATITUDE] > start[LATITUDE]:
        acc += "EAST"
    if end[LATITUDE] == start[LATITUDE]:
        acc += ''
    if end[LATITUDE] < start[LATITUDE]:
        acc += "WEST"
    return acc

def rent_bike(station_id: int, stations: List[list]) -> bool:
    """Update the available bike count and the docks available count
    for the station in stations with id station_id as if a single bike was
    removed, leaving an additional dock available. Return True if and only
    if the rental was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available - 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available + 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    """
    i = 0
    while i < len(stations):
        if stations[i][ID] == station_id:
            if stations[i][IS_RENTING] and stations[i][BIKES_AVAILABLE] > 0:
                stations[i][BIKES_AVAILABLE] -= 1
                stations[i][DOCKS_AVAILABLE] += 1
                return True
            else:
                return False
        i += 1

def return_bike(station_id: int, stations: List[list]) -> bool:
    """Update the available bike count and the docks available count
    for station in stations with id station_id as if a single bike was added,
    making an additional dock unavailable. Return True if and only if the
    return was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available + 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available - 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    """
    i = 0
    while i < len(stations):
        if stations[i][ID] == station_id:
            if stations[i][IS_RETURNING] and stations[i][DOCKS_AVAILABLE] > 0:
                stations[i][BIKES_AVAILABLE] += 1
                stations[i][DOCKS_AVAILABLE] -= 1
                return True
            else:
                return False
        i += 1

def calculate_goal_percentage(stations: List[list]) -> float:
    """Calculate the percentage of balancing all stations' bikes

    >>> calculate_goal_percentage(SAMPLE_STATIONS)
    0.5789473684210527
    >>> calculate_goal_percentage(HANDOUT_STATIONS)
    0.5434782608695652
    """
    i = 0
    total = 0
    current = 0
    while i < len(stations):
        total += stations[i][CAPACITY]
        current += stations[i][BIKES_AVAILABLE]
        i += 1
    goal_rate = current / total
    return goal_rate

def balance_all_bikes(stations: List[list]) -> int:
    """Calculate the percentage of bikes available across all stations
    and evenly distribute the bikes so that each station has as close to the
    overall percentage of bikes available as possible. Remove bikes from a
    station if and only if the station is renting and there is a bike
    available to rent, and return a bike if and only if the station is
    allowing returns and there is a dock available. Return the difference
    between the number of bikes rented and the number of bikes returned.

    >>> balance_all_bikes(HANDOUT_STATIONS)
    0
    >>> HANDOUT_STATIONS == [\
     [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 17, 14, True, True], \
     [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907, \
     15, 8, 7, True, True]]
    True
    """
    goal_rate = calculate_goal_percentage(stations)
    j = 0
    acc = 0
    while j < len(stations):
        rate = stations[j][BIKES_AVAILABLE] / stations[j][CAPACITY]
        if rate != goal_rate: #need modify
            goal_num = round(stations[j][CAPACITY] * goal_rate)
            if goal_num > stations[j][BIKES_AVAILABLE]: # need return
                diff = goal_num - stations[j][BIKES_AVAILABLE]
                require = stations[j][DOCKS_AVAILABLE] - diff
                if stations[j][IS_RETURNING] and require >= 0:
                    stations[j][BIKES_AVAILABLE] += diff
                    stations[j][DOCKS_AVAILABLE] -= diff
                    acc -= diff
                if stations[j][IS_RETURNING] and require < 0:
                    stations[j][BIKES_AVAILABLE] += stations[j][DOCKS_AVAILABLE]
                    stations[j][DOCKS_AVAILABLE] -= stations[j][DOCKS_AVAILABLE]
                    acc -= stations[j][DOCKS_AVAILABLE]
            if goal_num < stations[j][BIKES_AVAILABLE]: # need rent
                diff = abs(goal_num - stations[j][BIKES_AVAILABLE])
                require = stations[j][BIKES_AVAILABLE] - diff
                if stations[j][IS_RENTING] and require >= 0:
                    stations[j][BIKES_AVAILABLE] -= diff
                    stations[j][DOCKS_AVAILABLE] += diff
                    acc += diff
                if stations[j][IS_RENTING] and require < 0:
                    stations[j][BIKES_AVAILABLE] += stations[j][BIKES_AVAILABLE]
                    stations[j][DOCKS_AVAILABLE] -= stations[j][BIKES_AVAILABLE]
                    acc -= stations[j][BIKES_AVAILABLE]
        j += 1
    return acc

if __name__ == '__main__':
    pass

    # # To test your code with larger lists, you can uncomment the code below to
    # # read data from the provided CSV file.
    # stations_file = open('stations.csv')
    # bike_stations = csv_to_list(stations_file)
    # clean_data(bike_stations)

    # # For example,
    # print('Testing get_station_with_max_bikes: ', \
    #     get_station_with_max_bikes(bike_stations) == 7033)
