%Отбор георев по стороне и полу
female_hero(X,_) :- gender(X,female), organization(X,overwatch). 
male_hero(X,_) :- gender(X,male), organization(X,overwatch).
female_villian(X,_) :- gender(X,female), (organization(X,claw); organization(X, gang_of_the_dead)). 
male_villian(X,_) :- gender(X,male), organization(X,overwatch).

%Отбор только героев/злодеев/нейтральных
hero(X,_) :- organization(X, overwatch).
villian(X,_) :- organization(X, claw) ; organization(X, gang_of_the_dead).

%Отбор героев, актуальных в текущем сезоне 
meta_hero(X,_) :- (difficulty(X, easy) ; difficulty(X, medium)), not(tier(X, b); tier(X,c); tier(X,d)).

%Пермонажи с прописанной историей
have_backstory(X,_) :- cinematic(X, have), not(releas_year(X,2023)) , not(releas_year(X,2022)).