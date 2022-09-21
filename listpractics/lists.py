# List to practice
teams = ['Barcelona', 'Manchester United'];
goals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
year = [2010, 2011, 2012, 2013, 2014]

#how acess a list item
print(teams[0]);
print(teams[1]);

#how to combine diferent lists
print(f'{year[1]} champions league final {teams[0]} x {teams[1]} ended {goals[3]} {teams[0]} x {teams[1]} {goals[1]}')

#how modify a list value
teams[0] = 'Chelsea'
teams[1] = 'Bayern Muchen'

print(f'The {year[2]} champion was {teams[0]}, who beat {teams[1]} on penalties {goals[4]}-{3}, after drawing {goals[1]}-{goals[1]}in normal time.')

#list methods
pairs = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20];
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];

#how join lists
odds_and_pairs = pairs + odd;
print("sum two lists:",odds_and_pairs); #unsorted

#how join lists 2
pairs.extend(odd);
print("join with extends",pairs); #unsorted

#how add item to list
odds_and_pairs.append(20);
odds_and_pairs.append(21);
print(odds_and_pairs); #unsorted

#how add item to list with index
odds_and_pairs.insert(0, 'ABACAXI')
odds_and_pairs.insert(22, 'BANANA')
print(odds_and_pairs);

#how remove specified item list
odds_and_pairs.pop(0);
odds_and_pairs.pop(21);
print(odds_and_pairs);

#slice 
odds_and_pairs.insert(0, 'CACHORRO');
odds_and_pairs.insert(2, 'GATO');
odds_and_pairs.insert(5, 'CALANGO');
odds_and_pairs.insert(10, 'VACA');
odds_and_pairs.insert(16, 'BOLSONARISTA');
print(odds_and_pairs);

del(odds_and_pairs[:3:2]);
print(odds_and_pairs);
del(odds_and_pairs[3:9:6]);
print(odds_and_pairs);
del(odds_and_pairs[7:14:6]);
print(odds_and_pairs);


#get the higher number
print(max(odds_and_pairs));

#get the smaller number 
print(min(odds_and_pairs));

#generate list with range
new_list = list(range(1, 100));
print(new_list);

#generate all even numbers up to 100
even_list = list(range(0, 101, 2));
print(even_list);

#generate odd numbers up to 100
odd_numbers = list(range(1, 101, 2));
print(odd_numbers);

#clear lists
odds_and_pairs.clear();
print(odds_and_pairs);
