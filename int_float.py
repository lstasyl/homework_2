
#Функція що повертає квадрат числа
def square(value):
    return pow(value, 2)

#Функція яка повертає суму чисел
def sum_two_numbers(val_1, val_2):
    return val_1 + val_2

#Функція яка повертає цілу частину і залишок.
def divide_and_remainder(val_1, val_2):
    quotient = val_1 // val_2
    remainder = val_1 % val_2
    return quotient, remainder

#тест для square
assert square(0.5) == 0.25, 'Test 1'
assert square(-0.5) == 0.25, 'Test 2'
assert square(-5) == 25, 'Test 3'
assert square(10) == 100, 'Test 4'

#тест для sum_two_numbers
assert sum_two_numbers(10, -5) == 5, 'Test 1'
assert sum_two_numbers(3.5, 2.5) == 6.0, 'Test 2'

#тест для divide_and_remainder
assert divide_and_remainder(10, 3) == (3, 1), 'Test 1'
assert divide_and_remainder(10, -3) == (-4, -2), 'Test 2'
assert divide_and_remainder(-10, 3) == (-4, 2), 'Test 3'
assert divide_and_remainder(-10, -3) == (3, -1), 'Test 4'

print("Ok")

