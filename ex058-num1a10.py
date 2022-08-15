import random

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#numSort = random.randint(0, len(aluno)-1)
num = random.choice(num)
cont = 0
numero = 0

while numero != num:
    numero = int(input('Digite um numero entre 1 a 10: '))
    cont += 1

if numero == num:
    print('\nVocê venceu em {} tentativas'.format(cont))
# else:
#     print('\nVocê perdeu')