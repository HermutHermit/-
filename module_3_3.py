def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(25, 'salt')
print_params(True)
print_params(b ='card')
print_params(963, 'cat', c = False)

print_params(b = 25)
print_params(c = [1, 2, 3])
print('_________________________________________________')

values_list = [181298, 'Sveta', True]
values_dict = {'a': 12, 'b': False, 'c': 'table'}
print_params(*values_list)
print_params(**values_dict)
print('_________________________________________________')
values_list_2 = [18, 'book']
print_params(*values_list_2, 42)