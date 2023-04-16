# import necessary packages 
from pyswip.prolog import Prolog
from pyswip.easy import *

prolog = Prolog()  # create a Prolog instance


# define answer options for each question
options = {   
    'meal_size': ['snack', 'proper_meal'],
    'type_of_snack': ['sweet', 'savory'],
    'distance_to_travel': ['less_than_5km', 'more_than_5km'],
    'type_of_cuisine': ['chinese', 'indian', 'vietnamese', 'japanese', 'argentinian'],
    'budget': ['less_than_25usd', 'more_than_25usd'],
    'dietary_type': ['vegetarian', 'vegan', 'omnivore'],
    'vibe_wanted': ['casual', 'formal'],
    'how_many_people': ['less_than_5', 'more_than_5'],
}

options_english = { # for printing purposes
    'snack': 'snack',
    'proper_meal': 'proper meal',
    'sweet': 'sweet',
    'savory': 'savory',
    'less_than_5km': 'less than 5km',
    'more_than_5km': 'more than 5km',
    'chinese': 'Chinese',
    'indian': 'Indian',
    'vietnamese': 'Vietnamese',
    'japanese': 'Japanese',
    'argentinian': 'Argentinian',
    'more_than_25usd': 'more than 25 USD',
    'less_than_25usd': 'less than 25 USD',
    'vegetarian': 'vegetarian',
    'vegan': 'vegan',
    'omnivore': 'omnivore',
    'casual': 'casual',
    'formal': 'formal',
    'less_than_5': 'less than 5 people',
    'more_than_5': 'more than 5 people',
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
    'ice_cream': {'name': 'Rapa Nui',
                    'link': 'https://rapanui.com.ar/'},
    'empaluna': {'name': 'Empaluna',
                    'link': 'https://www.instagram.com/empaluna/?hl=en'},
    
    'un_cuenco_chino': {'name': 'Un Cuenco Chino',
                          'link': 'https://www.facebook.com/Un-Cuenco-chino-246259128847895/'},
    'delhi_mahal': {'name': 'Delhi Mahal',
                          'link': 'https://www.facebook.com/pages/Delhi-Mahal/202198679931369'},
    'in_n_out_sushi': {'name': 'In n Out Sushi',
                          'link': 'https://www.instagram.com/inandoutsushi/?hl=en'},
    'santos_manjares': {'name': 'Santos Manjares',
                            'link': 'https://www.facebook.com/santosmanjares/'},             
    'saigon_noodle_bar': {'name': 'Saigon Noodle Bar',
                            'link': 'https://www.saigonargentina.com/'}, 
    
    'koko_bao': {'name': 'Koko Bao',
                'link': 'https://www.kokobaobar.com/'},
    'don_julio': {'name': 'Don Julio',
                    'link': 'https://www.parrilladonjulio.com/'},
    
    'chui': {'name': 'Chui',
                'link': 'https://www.instagram.com/chui.ba/?hl=en'},
    'sampa': {'name': 'Sampa',
                'link': 'https://www.sampa.com.ar/'},
 
    'xi_bei_feng' : {'name': 'Xi Bei Feng',
                        'link': 'https://www.xibeifeng.com.ar/'},
    'punch_curry_bar': {'name': 'Punch Curry Bar',
                        'link': 'https://www.punchcurrybar.com/'},
    'cang_tin': {'name': 'Cang Tin',
                    'link': 'https://www.instagram.com/cangtinba/?hl=en'},
    'mirutaki_ramen_and_sushi': {'name': 'Mirutaki Ramen and Sushi',
                                    'link': 'https://www.tripadvisor.com/Restaurant_Review-g312741-d13510648-Reviews-Mirutaki-Buenos_Aires_Capital_Federal_District.html'},
    'las_cabras' : {'name': 'Las Cabras',
                    'link': 'https://www.tripadvisor.com/Restaurant_Review-g312741-d1187741-Reviews-Las_Cabras-Buenos_Aires_Capital_Federal_District.html'},
    
    'koi_dumplings_palermo': {'name': 'Koi Dumplings Palermo', 
                              'link': 'https://koidumplings.com/'},
    'tandoor': {'name': 'Tandoor',
                'link': 'https://www.tandoor.com.ar/'},
    'green_bamboo': {'name': 'Green Bamboo',
                        'link': 'https://www.instagram.com/greenbambooargentina/?hl=en'},
    'donnet': {'name': 'Donnet',
                'link': 'https://www.instagram.com/donnet_te_ama},'}
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


def show_options(question):
    """Print out the options for a given question. It prints it out in nice English format.
    
    Args:
        question (str): The question to print out the options for.

    Returns:
        None
        """

    print("Please choose one of the following options:")
    for index, option in enumerate(options[question]):
        print(f'\t{str(index + 1)} : {options_english[option]}')
    print("---------------------------------------------")


def main():
    """Main function to run the program."""

    while True: # keeps repeating until user enters 'n' to stop the program
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
     
            try_again = input("\nDo you want to use the app again (y/n)? ")
            if try_again == 'y':
                continue
            elif try_again == 'n':
                print("Thank you for using our service!")
                break
        else:
            print("\nUnfortunately, we could not find a restaurant that matches your criteria.")
            try_again = input("\nDo you want to use the app again (y/n)? ")
            if try_again == 'y':
                continue
            elif try_again == 'n':
                print("Thank you for using our service!")
                break

if __name__ == "__main__":
    main()