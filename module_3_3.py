def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(2)
print_params(75, False)
print_params(b=True)
print_params(b=5, c='Встреча')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [54.55, 'Список', 80]
values_dict = {'a': 5, 'b': 'Студент', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [22, 'Inkubator']
print_params(*values_list_2)