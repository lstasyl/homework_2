
#Функція яка повертає середнє значення чисел
def calculate_average(some_list):
    if not some_list:
        return 0
    return sum(some_list)/len(some_list)

#Функція яка повертає спільні елементи двох листів
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))



#Тести для calculate_average
assert calculate_average([1, 2, 3, 4, 5]) == 3.0, 'Test 1'
assert calculate_average([0.5, 1.5, 2.5, 3.5, 4.5]) == 2.5, 'Test 2'
assert calculate_average([-1, 0, 1]) == 0.0, 'Test 3'

#Тести для find_common_elements
assert find_common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]) == [4, 5], 'Test 1'
assert find_common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3], 'Test 2'
assert find_common_elements([], []) == [], 'Test 3'
assert find_common_elements([1, 2, 3], [4, 5, 6]) == [], 'Test 4'
assert find_common_elements([1, 2, 3], [3, 4, 5]) == [3], 'Test 5'


print("Ok")
