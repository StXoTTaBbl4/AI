X = ["0","1"].
get_recomendation(Role,Hours_in_game) :- if Hours_in_game < 20 and Role = tank then 
											print(X).
												
%TODO добавить массивы отсортированных по часам персонажей