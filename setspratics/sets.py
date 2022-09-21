#create set
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
name = set()


#how interact with sets
for v in set1:
    print(v)


#how add items in a set
set1.add(0);
name.add('José');
name.add('Duarte');

print(set1);
print(name);

#remove set item
name.discard('José');
print(name);

#set can remove a list duplicated item
list_dup = [1, 2, 1, 3, 2, 1, 1, 3, 5, 4, 5]
print(list_dup);
remove_dup = set(list_dup);
print(remove_dup);
list_not_duplicated = list(remove_dup);
print(list_not_duplicated);
print(list_not_duplicated[4])

#union sets
even = {0, 2, 4, 6, 8, 10}
one_to_twenty = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
odds = {21, 23, 25}

union = even | one_to_twenty | odds
print(union);

#intersection sets
prime = {2, 3, 5, 7, 9, 11, 13, 17, 'test'}
one_to_ = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 'test'}

intersection = prime & one_to_
print("intersection =", intersection)

#diference sets
numbersA =  {1, 2, 3, 4, 5};
numbersB = {4, 5, 6, 7, 8, 9};

print('Only A =', numbersA - numbersB);
print('Only B =', numbersB - numbersA);

#simetric difference
print('in A but not in B AND in B but not in A', numbersA ^ numbersB);