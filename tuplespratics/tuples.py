# tuples can't be edited
#way 1 to create tuple
from asyncio import ensure_future


english_teams_tuple = ('manchester united', 'chelsea', 'liverpool', 'arsenal'); 
#way 2 to create tuple
spanish_teams_tuple = 'Barcelona', 'real madrid', 'villa real', 'sevilla'

#how acess tuple item
print(english_teams_tuple[3]);

#interact in tuple
for team in english_teams_tuple:
    if team == 'manchester united':
        print(f'{team} was finalist in 2008, 2009, 2011');
    elif team == 'chelsea':
        print(f'{team} was finalist in 2008, 2012, 2021');
    elif team == 'liverpool':
        print(f'{team} was finalist in 2006, 2007, 2018');
    elif team == 'arsenal':
        print(f'{team} was finalist in 2005');


#concat two tuples
one_to_five =  tuple(range(1, 5));
six_to_ten = tuple(range(6, 10));
print(one_to_five);
print(six_to_ten);

print( one_to_five + six_to_ten);

#repeat/muitply a tuple n times
print(english_teams_tuple * 5)

#convert a tuple to list
english_teams_tuple = list(english_teams_tuple)
print(english_teams_tuple)

#after convert a tuple to list, we can edit them
english_teams_tuple[2] = 'tottenham'
print(english_teams_tuple)

#convert list to tuple
english_teams_tuple = tuple(english_teams_tuple)
print(english_teams_tuple)