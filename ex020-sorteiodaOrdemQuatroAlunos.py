#sortear a ordem dos 4 alunos para apagar o quadro. programa ler o nome e escolher o nome escolhido

import random

#aluno = ['joao', 'pedro', 'lucas', 'gabriel']
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

aluno = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(aluno)

print('Ordem foi: ',aluno)
