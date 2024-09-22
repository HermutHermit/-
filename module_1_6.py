# Словарь ↓
my_dict = {'Anna' : 1985, 'Alex' : 1977, 'Sasha' : 1992}
print (my_dict)
print (my_dict['Alex'])
print (my_dict.get ("Liza"))
my_dict.update ({'Masha' : 1999,
                 "Kirill" : 2006})
print (my_dict)
print (my_dict.pop ("Anna"))
print (my_dict)

# Множество ↓
my_set = {1,15,36,15,42, "cat", 12, 'red', 'card', 'cat', 36, 12}
my_set.update(['Cole', 125698])
print(my_set)
my_set.discard (15)
print(my_set)