# import necessary packages
from pyswip.prolog import Prolog
from pyswip.easy import *

prolog = Prolog()  # create a Prolog instance


# define answer options for each question
options = {   
    'meal_size': ['snack', 'proper_meal'],
    'type_of_snack': ['sweet', 'savory'],
    'distance_to_travel': ['less_than_5km', 'more_than_5km'],
    'type_of_cuisine': ['chinese', 'indian', 'vietnamese', 'cajun', 'japanese'],
    'budget': ['more_than_25usd', 'less_than_25usd'],
    'dietary_type': ['vegetarian', 'vegan', 'omnivore'],
    'vibe_wanted': ['casual', 'fine_dining'],
    'how_many_people': ['<5', '>5'],
}

# define prompts for each question
prompts = {  
    'meal_size': 'Do you want a large meal or a snack?',
    'type_of_snack': 'Do you want a sweet or savory snack?',
    'distance_to_travel': 'How far are you willing to travel?',
    'budget': 'How much do you want to spend?',
    'dietary_type': 'What is your dietary type?',
    'vibe_wanted': 'Do you want something more casual or fine dining experience?',
    'how_many_people': 'How many people are you going with?',
    'type_of_cuisine': 'What type of cuisine do you prefer?',
}

# dictionary of restaurant names and links 
restaurant_recommendations = {
    'ice_cream': {'name': 'Ice Cream',
                    'link': ''},
    'empanada': {'name': 'Empanada',
                    'link': ''},
    'un_cueno_chino': {'name': 'Un Cueno Chino',
                          'link': ''},
    'delhi_mahal': {'name': 'Delhi Mahal',
                          'link': ''},
    'salgon_noodle_bar': {'name': 'Salgon Noodle Bar',
                            'link': ''}, 
    'sacro': {'name': 'Sacro',
                'link': ''},
    'don_julio': {'name': 'Don Julio',
                    'link': ''},
    'chui': {'name': 'Chui',
                'link': ''},
    'sampa': {'name': 'Sampa',
                'link': ''},
    'gran_dabbang': {'name': 'Gran Dabbang',
                        'link': ''},
    'bao': {'name': 'Bao',
            'link': ''},
    'himitsu_kichi': {'name': 'Himitsu Kichi',
                        'link': ''},
    'las_galgos_bar': {'name': 'Las Galgos Bar',
                        'link': ''},
    'nola': {'name': 'Nola',
                'link': ''}, 
    'calden_del_soho': {'name': 'Calden Del Soho',
                        'link': ''},
}


# Define foreign function to read user input
def read_py(A, V, Y):
    if isinstance(Y, Variable):
        # Check if the user has already answered this question. If not, ask it.
        if str(A) not in user_answers.keys():
            print('\n\n')
            print('---------------------------------------------')
            print(prompts[str(A)]) # print out the prompt for the question
            print('---------------------------------------------')
            show_options(str(A))  # print out the options (available answers) for the question
            while True: # keep asking until user enters a valid number (1, 2, 3, etc.)
                picked_option = input("Enter the number for your choice: ") # get user's response
                # check if the user's response is a valid number (one of the available options)
                if int(picked_option) in range(1, len(options[str(A)]) + 1): 
                    break
                else:
                    print("Please enter one of the available numbers [1, 2, 3, etc.]")  
            user_answers[str(A)] = options[str(A)][int(picked_option) - 1] # store the user's response
        # if user's response is the variable V Prolog is looking for, unify to yes.
        # if not, unify no
        if user_answers[str(A)] == str(V):
            response = 'yes'
        else:
            response = 'no'
        # unify the user's response to the variable Y
        Y.unify(Atom(response))
        return True
    else: # if Y is not a variable, return False
        return False 


def show_options(strings):

    print("Please choose one of the following options:")
    for index, option in enumerate(options[strings]):
        print(f'\t{str(index + 1)} : {option}')
    print("---------------------------------------------")


def main():
    global user_answers
    user_answers = {}  # store user responses to questions
    # Define predicates
    retractall = Functor("retractall") # remove all items from Knowledge Base
    known = Functor("known", 3) # predicate for storing user responses

    read_py.arity = 3 # set the arity of the foreign function
    registerForeign(read_py) # register the foreign function

    # get the path to the KB file
    try: 
        prolog.consult("KB.pl") # load the KB file (make sure you open the entire folder so it runs)
        call(retractall(known))  # remove all items from Knowledge Base
    except Exception as e:
        print(e)
        print("Please make sure you have the KB file in the same folder as this file.")
        return
    
    recommendations = [s for s in prolog.query("recommendation(X).")]  # get recommendation

    # printing out the recommendation
    if recommendations:
        print(f"\nGreat news! We found a perfect match to your choices. You should try out {restaurant_recommendations[recommendations[0]['X']]['name']}!")
        print(f"This is the link to the restaurant: {restaurant_recommendations[recommendations[0]['X']]['link']}\n")
    else:
        print("\nUnfortunately, we could not find a restaurant that matches your criteria.")
        while True:
            try_again = input("\nDo you want to try again (y/n)? ")
            if try_again == 'y':
                main()
            elif try_again == 'n':
                print("Thank you for using our service!")
                break
            else:
                print("Please enter either 'y' or 'n'")

if __name__ == "__main__":
    main()