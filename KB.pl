%  Tell prolog that known/3 will be added later
:- dynamic known/3.
:- discontiguous dietary_type/1. % it is okay for the dietary_type not to be next to one another
:- discontiguous vibe_wanted/1. % it is okay for the vibe_wanted not to be next to one another

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
% if a user is vegetarian, the user can eat vegan food too
 dietary_type(vegan) :- dietary_type(vegetarian).
% CHANGE: Define not_formal condition
vibe_wanted(not_formal) :- \+ vibe_wanted(formal).

% Restaurant Recommendations
% Note all restaurants have vegan options, so dietary_type is not required here
recommendation(ice_cream) :- meal_size(snack), type_of_snack(sweet).
recommendation(empaluna) :- meal_size(snack), type_of_snack(savory).

recommendation(un_cuenco_chino) :- meal_size(proper_meal), distance_to_travel(less_than_5km), type_of_cuisine(chinese). 
recommendation(delhi_mahal) :- meal_size(proper_meal), distance_to_travel(less_than_5km), type_of_cuisine(indian). 
recommendation(in_n_out_sushi) :- meal_size(proper_meal), distance_to_travel(less_than_5km), type_of_cuisine(japanese). 
recommendation(saigon_noodle_bar) :- meal_size(proper_meal), distance_to_travel(less_than_5km), type_of_cuisine(vietnamese). 
recommendation(santos_manjares) :- meal_size(proper_meal), distance_to_travel(less_than_5km), type_of_cuisine(argentinian). 

recommendation(koko_bao) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(less_than_25usd), dietary_type(vegan).
recommendation(don_julio) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(less_than_25usd), dietary_type(omnivore).

recommendation(chui) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(omnivore), vibe_wanted(formal), how_many_people(less_than_5).
recommendation(sampa) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(omnivore), vibe_wanted(formal), how_many_people(more_than_5).

recommendation(xi_bei_feng) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(omnivore), vibe_wanted(casual), type_of_cuisine(chinese).
recommendation(punch_curry_bar) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(omnivore), vibe_wanted(casual), type_of_cuisine(indian).
recommendation(cang_tin) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(omnivore), vibe_wanted(casual), type_of_cuisine(vietnamese).
recommendation(mirutaki_ramen_and_sushi) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(omnivore), vibe_wanted(casual), type_of_cuisine(japanese).
recommendation(las_cabras) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(omnivore), vibe_wanted(casual), type_of_cuisine(argentinian).

recommendation(koi_dumplings_palermo) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(vegan), type_of_cuisine(chinese).
recommendation(koi_dumplings_palermo) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(vegan), type_of_cuisine(japanese).
recommendation(tandoor) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(vegan), type_of_cuisine(indian).
recommendation(green_bamboo) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(vegan), type_of_cuisine(vietnamese).
recommendation(donnet) :- meal_size(proper_meal), distance_to_travel(more_than_5km), budget(more_than_25usd), dietary_type(vegan), type_of_cuisine(argentinian).

% Asking clauses
ask(A, V):-
known(yes, A, V), % succeed if true
!.	% stop looking

ask(A, V):-
known(_, A, V), % fail if false
!, fail.

% if it is already known to be something else, the user does not need to be asked again
ask(A, V):-
known(yes, A, V2),
V \== V2,
!, fail.

ask(A, V):-
read_py(A,V,Y), % obtain the answer with that python function
assertz(known(Y, A, V)), % save it for future reference
Y == yes.	% succees or fail
