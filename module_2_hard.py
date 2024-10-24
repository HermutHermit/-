import random

n = random.randint(3, 20)
print(n)
def get_password(number):
    password = ''
    for i in range(1, n):
        for j in range(2, n):
            if j <= i:
                continue
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password
result = get_password(n)
print('Пароль:', result)