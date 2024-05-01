
#Функцію, яка перевіряє, чи є одна множина підмножиною іншої

def is_subset(sets1, sets2):
    sets1 = {1, 2}
    sets2 = {1, 2, 3, 4, 5}
    assert is_subset(sets1, sets2) == True, 'Test 1'

    sets3 = {1, 2, 6}
    assert is_subset(sets1, sets3) == False, 'Test 2'

    sets4 = {1, 'a', (2, 3)}
    sets5 = {'b', 'c', 3.14}
    assert is_subset(sets4, sets5) == False, 'Test 3'


#Функція яка приймає дві множини і повертає їхнє об'єднання
def union_of_sets(set1, set2):
    return set1.union(set2)

set1 = {3, 4, 5}
set2 = {1, 2, 3}
expected_result = {1, 2, 3, 4, 5}
assert union_of_sets(set1, set2) == expected_result, 'Test 1'

set3 = {1, 'a', (2, 3)}
set4 = {'b', 'c', 3.14}
expected_result = {1, 'a', (2, 3), 'b', 'c', 3.14}
assert union_of_sets(set3, set4) == expected_result, 'Test 2'


print('OK')
