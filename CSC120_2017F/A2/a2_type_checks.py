""" This module should be used to test the parameter and return types of the
functions in a2_functions.py. Before submitting your assignment, run this
type-checker. If errors occur when you run this module, fix them before you
submit your assignment.  

When this module runs, if only "okay" is displayed, then the type checks passed.
This means that the function parameters and return types match the assignment
specification, but it does not mean that your code works correctly in all situations.
Be sure to test your code thoroughly before submitting."""

import a2_functions

if __name__ == '__main__':
    
    # Type check a2_functions.load_profiles
    profiles_file = open('profiles.txt')
    person_to_friends = {}
    person_to_networks = {}
    
    result = a2_functions.load_profiles(profiles_file, person_to_friends, 
        person_to_networks)
    assert isinstance(result, type(None)), \
    '''a2_functions.load_profiles should return None, 
    but returned type {0}.'''.format((type(result)))
    
    
    # Type check a2_functions.invert_networks_dict
    person_to_networks = {
    'Cameron Tucker': ['Clown School', 'Wizard of Oz Fan Club'],
    'Gloria Pritchett': ['Parent Teacher Association']}
    
    result = a2_functions.invert_networks_dict(person_to_networks)
    assert isinstance(result, dict),\
    '''a2_functions.invert_networks_dict should return a 
    dict of {str : list of str}, but returned type {0}'''.format((type(result)))

    # Checking the types of the dictionary's keys and values.
    for (key, value) in result.items():    

        assert isinstance(key, str),\
        '''a2_functions.invert_networks_dict should return a 
        dict of {str : list of str}
        but a key in the dict has type {0}.'''.format((type(key)))

        assert isinstance(value, list),\
        '''a2_functions.invert_networks_dict should return a 
        dict of {str : list of str}
        but a value in the dict has type {0}.'''.format(type(value))

        # Checking the types of items in the dictionary's values lists.
        for item in value:
            assert isinstance(item, str),\
            '''a2_functions.invert_networks_dict should return a 
            dict of {str : list of str}, but an item in a values list
            has type {0}.'''.format((type(item)))
            
            
    # Type check a2_functions.make_recommendations
    person = 'Claire Dunphy'

    person_to_friends = {
    'Jay Pritchett': ['Gloria Pritchett', 'Manny Delgado', 'Claire Dunphy'], 
    'Claire Dunphy': ['Phil Dunphy', 'Mitchell Pritchett', 'Jay Pritchett'], 
    'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], 
    'Mitchell Pritchett': ['Claire Dunphy', 'Cameron Tucker', 'Luke Dunphy'], 
    'Alex Dunphy': ['Luke Dunphy'], 
    'Cameron Tucker': ['Mitchell Pritchett', 'Gloria Pritchett'], 
    'Haley Gwendolyn Dunphy': ['Dylan D-Money'], 
    'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 
    'Dylan D-Money': ['Haley Gwendolyn Dunphy'], 
    'Gloria Pritchett': ['Jay Pritchett', 'Cameron Tucker', 'Manny Delgado'], 
    'Luke Dunphy': ['Manny Delgado', 'Alex Dunphy', 
    'Phil Dunphy', 'Mitchell Pritchett']}

    person_to_networks = {
    'Phil Dunphy': ['Real Estate Association'], 
    'Claire Dunphy': ['Parent Teacher Association'], 
    'Manny Delgado': ['Chess Club'], 
    'Mitchell Pritchett': ['Law Association'], 
    'Alex Dunphy': ['Orchestra', 'Chess Club'], 
    'Cameron Tucker': ['Clown School', 'Wizard of Oz Fan Club'], 
    'Gloria Pritchett': ['Parent Teacher Association']}
    
    result = a2_functions.make_recommendations(
        person, person_to_friends, person_to_networks)
    assert isinstance(result, list),\
    '''a2_functions.make_recommendations should return 
    a list of (str, int) tuple, but returned {0}.'''.format(type(result))

    for (name, score) in result:    
        assert isinstance(name, str),\
        '''a2_functions.make_recommendations should return a 
        list of (str, int) tuple, but the first element of a
        tuple has type {0}.'''.format((type(name)))
        
        assert isinstance(score, int),\
        '''a2_functions.make_recommendations should return a 
        list of (str, int) tuple, but the second element of a 
        tuple has {0}.'''.format((type(score)))
        
        
    # Type check a2_sort_recommendations
    recommendations_list = [('Cameron Tucker', 1), ('Manny Delgado', 1)]
    
    result = a2_functions.sort_recommendations(recommendations_list)
    assert isinstance(result, list),\
    '''a2_functions.sort_recommendations should return a list of str,
     but returned type {0}.'''.format((type(result)))
    
    for item in result:
        assert isinstance(item, str),\
        '''a2_functions.sort_recommendations should return a list of str,
         but a list item has type {0}.'''.format((type(item)))

    print("okay")
