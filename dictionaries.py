
#Функція яка приймає словник і виводить всі ключі цього словника
def print_keys(dictionary):
    keys = ""
    for key in dictionary.keys():
        keys += key
    return keys if keys else None


#Функція яка приймає два словника і повертає новий об'єднаний словник
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


#тест для print_keys
test_dict1 = {}
assert print_keys(test_dict1) == None, 'Test 1'

test_dict2 = {'a': 1}
assert print_keys(test_dict2) == 'a', 'Test 2'

test_dict3 = {'a': 1, 'b': 2, 'c': 3}
assert print_keys(test_dict3) == 'a''b''c', 'Test 3'

#тест для merge_dictionaries
tst_dict1 = {'c': 3, 'd': 4}
tst_dict2 = {'a': 1, 'b': 2}
expected_result2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
assert merge_dictionaries(tst_dict1, tst_dict2) == expected_result2, 'Test 1'

tst_dict3 = {'a': 10, 'b': 20}
tst_dict4 = {'a': 30, 'b': 40}
expected_result2 = {'a': 30, 'b': 40}
assert merge_dictionaries(tst_dict3, tst_dict4) == expected_result2, 'Test 2'

print('OK')
