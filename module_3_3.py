def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# 1
print('\n1.Функция с параметрами по умолчанию:\n')
print_params()
print_params(a = False)
print_params(a = 'строка', b = 'False')
print_params(a = 10, b = True, c = False )
print_params(b = 25)
print_params(c = [1,2,3])

# 2
print('\n2.Распаковка параметров:\n')
values_list = ['List', False, 44]
values_dict = {'a': 55, 'b': 'Dict', 'c': True }
print_params(*values_list)
print_params(**values_dict)

# 3
print('\n3.Распаковка + отдельные параметры:\n')
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)