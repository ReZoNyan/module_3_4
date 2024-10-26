# Задание № 1
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(3, 4, 5)
print_params('строка')
print_params(1, 'строка', True)
print_params(b=25, c=[1, 2, 3])
print('\n')

# Задание № 2
values_list = [2.25, True, 'ST']
values_dict = {'a': True, 'b': 45.55, 'c': 'dict'}
print_params(*values_list)
print_params(**values_dict)
print('\n')

# Задание № 3
values_list_2 = [False, 0.23]
print_params(*values_list_2, 42)