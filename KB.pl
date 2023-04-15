%  Tell prolog that known/3 will be added later
:- dynamic known/3.

% Askables
meal_size(X) :- ask(meal_size, X).
type_of_snack(X) :- ask(type_of_snack, X).
distance_to_travel(X) :- ask(distance_to_travel, X).
type_of_cuisine(X) :- ask(type_of_cuisine, X).
budget(X) :- ask(budget, X).
dietary_type(X) :- ask(dietary_type, X).
vibe_wanted(X) :- ask(vibe_wanted, X).
how_many_people(X) :- ask(how_many_people, X).

% Other Rules 
% if the person is an omnivore, the user can eat vegan and vegetarian food too
dietary_type(vegetarian) :- dietary_type(omnivore).
dietary_type(vegan) :- dietary_type(omnivore).
% if a user is vegetarian, the user can eat vegan food too
dietary_type(vegan) :- dietary_type(vegetarian).

% Restaurant Recommendations
% Note all restaurants have vegan options, so dietary_type is not required here
recommendation(ice_cream) :- meal_size(snack), type_of_snack(sweet).
recommendation(empanada) :- meal_size(snack), type_of_snack(savory).
recommendation(un_cueno_chino) :- meal_size(proper_meal), distance_to_travel(less_than_5km), type_of_cuisine(chinese). 
recommendation(delhi_mahal) :- meal_size(proper_meal), distance_to_travel(less_than_5km), type_of_cuisine(indian). 
recommendation(sacro) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(less_than_25usd), dietary_type(omnivore).
recommendation(bao) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(less_than_25usd), dietary_type(vegetarian).
recommendation(don_julio) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(less_than_25usd), dietary_type(vegan).
recommendation(chui) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(omnivore), vibe_wanted(fine_dining), how_many_people(less_than_5).
recommendation(sampa) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(omnivore), vibe_wanted(fine_dining), how_many_people(more_than_5).
recommendation(los_galgos_bar) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(omnivore), vibe_wanted(casual), type_of_cuisine(argentinian).
recommendation(gran_dabbang) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(omnivore), vibe_wanted(casual), type_of_cuisine(indian).
recommendation(himitsu_kichi) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(vegetarian), vibe_wanted(formal).
recommendation(himitsu_kichi) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(vegan), vibe_wanted(formal), type_of_cuisine(japanese).
recommendation(calden_del_soho) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(vegan), vibe_wanted(formal), type_of_cuisine(argentinian).
recommendation(dhaba) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(vegan), vibe_wanted(casual), type_of_cuisine(middle_eastern).
recommendation(nola) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(vegetarian), vibe_wanted(casual).
recommendation(nola) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(vegan), vibe_wanted(casual), type_of_cuisine(cajun).

% Asking clauses
ask(A, V):-
known(yes, A, V), % succeed if true
!.	% stop looking

ask(A, V):-
known(_, A, V), % fail if false
!, fail.

% if it is already known to be something else, the user doesn't need to be asked again
ask(A, V):-
known(yes, A, V2),
V \== V2,
!, fail.

ask(A, V):-
read_py(A,V,Y), % obtain the answer with that python function
assertz(known(Y, A, V)), % save it for future reference
Y == yes.	% succees or fail
