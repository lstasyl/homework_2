
#Функцію, яка приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне
def is_even(number):
    return (number & 1) == 0

#функцію, яка приймає список чисел і повертає новий список, що містить тільки парні числа.
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

#Тести для is_even
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

#Тести для filter_even_numbers
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
expected_result1 = [2, 4, 6, 8, 10]
assert filter_even_numbers(numbers1) == expected_result1, 'Test1'

numbers2 = [1, 3, 5, 7, 9]
expected_result2 = []
assert filter_even_numbers(numbers2) == expected_result2, 'Test2'
print('Ok')
