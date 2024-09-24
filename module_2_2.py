first = input ('Введите целое число: ')
second = input ('Введите целое число еще раз: ')
third = input ('Введите целое число последний раз: ')

if  first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print (2)
else:
    print (0)
