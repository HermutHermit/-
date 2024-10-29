calls = 0
def count_calls ():
    global calls
    calls+=1
def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
print(string_info('Axolotl'))
print(string_info('Ankylosaurus'))
print(is_contains('Achatina', ['ha', 'tina', 'aCHaTiNa']))
print(is_contains('Moonshine', ['shine', 'moon']))
print(is_contains('Bumblebee', ['bee', 'bumble', 'fly']))
print(string_info('Ichthyornis'))
print(calls)