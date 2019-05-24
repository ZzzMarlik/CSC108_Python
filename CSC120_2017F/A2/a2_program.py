import a2_functions
from a2_functions import load_profiles, make_recommendations, sort_recommendations

if __name__ == '__main__':

    # Use these messages in your code below.
    prompt_msg = "Please enter a person (or press return to exit): "
    no_recommendations_msg = "There are no recommendations for this person."
    exit_msg = "Thank you for using the recommendation system!"

    # During testing, we may change the values of these variables to non-empty
    # dictionaries or to different files.
    friendships = {}
    networks = {}

    profiles_file = open('profiles.txt')

    # Add your code here.
    load_profiles(profiles_file, friendships, networks)
    print(friendships)
    person = input(prompt_msg)
    while person != '':
        potential = make_recommendations(person, friendships, networks)
        display = sort_recommendations(potential)
        if len(display) > 0:
            for name in display:
                print(name)
        else:
            print(no_recommendations_msg)
        person = input('\n' + prompt_msg)
    print(exit_msg)
    profiles_file.close()
