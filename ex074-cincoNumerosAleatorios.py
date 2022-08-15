import random
numeros = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))

print('-='*15)
print(numeros)
print(sorted(numeros))
print(f'O maior foi {sorted(numeros)[-1]} e menor foi {sorted(numeros)[0]}')
print('-='*15)


# for i in range(0,4):
#     # numeros = tuple(random.randint(0,10))
#     print(f'{numeros}', end=' ')
#
# for i in range(0, 5):
#     aleatorio = str(random.randint(0,10))
#     numeros = numeros + tuple(aleatorio)
#
# print(numeros)
# print('-=' * 25)

