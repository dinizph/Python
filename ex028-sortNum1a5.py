import random

numero = int(input('Digite um numero entre 1 a 5: '))

num = [0, 1, 2, 3, 4, 5]
#numSort = random.randint(0, len(aluno)-1)
num = random.choice(num)

if numero == num:
    print('Você venceu')
else:
    print('Você perdeu')