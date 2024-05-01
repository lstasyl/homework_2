
#Функція яка повертає довжину рядка
def len_str(string):
    return len(string)

#Функція яка повертає об'єднаний рядок
def combine_strings(string_1, string_2):
    return string_1+string_2

#Тести для функції len_str
assert len_str("") == 0, 'Test 1'
assert len_str("Hello, world!") == 13, 'Test 2'
assert len_str("1234567890") == 10, 'Test 3'
assert len_str(" ") == 1, 'Test 4'

#Тести для функції combine_strings
assert combine_strings("Hello", "world") == "Helloworld", 'Test 1'
assert combine_strings("", "world") == "world", 'Test 2'
assert combine_strings("Hello", "") == "Hello", 'Test 3'
assert combine_strings("", "") == "", 'Test 4'
assert combine_strings("123", "456") == "123456", 'Test 5'
print("ОК")
