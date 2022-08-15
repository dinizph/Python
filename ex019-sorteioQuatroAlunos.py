#sortear um dos 4 alunos para apagar o quadro. programa ler o nome e escolher o nome escolhido
import random

#aluno = ['joao', 'pedro', 'lucas', 'gabriel', 'renan']
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

aluno = [aluno1, aluno2, aluno3, aluno4]
#numSort = random.randint(0, len(aluno)-1)
numSort = random.choice(aluno)


print('Aluno sorteado foi: ',numSort)

#DADO
# import random
# 
# aluno = ['1', '2', '3', '4', '5', '6']
# numSort = random.randint(0, len(aluno)-1)
# 
# 
# print('Numero sorteado no dado foi: ',aluno[numSort])
