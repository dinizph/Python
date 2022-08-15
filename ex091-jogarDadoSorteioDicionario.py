#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from operator import itemgetter
jogador = {}
Jogadores = []

for i in range(1,5):
        jogador['Nome'] = "jogador"+str(i)
        jogador['Pontos'] = randint(1,6)
        Jogadores.append((jogador.copy()))
print('='*20)
# print(Jogadores)
for j in Jogadores:
    # print(j)
    for v in j.values():
        print(f'{v}', end=' ')
    print()

ranking = sorted(Jogadores, key=itemgetter('Pontos'), reverse=True)
# print(novosJogadores)
print('='*20)
for j in ranking:
    print(j)

print('='*20)
for i, (j, p) in enumerate(ranking):
    print(f' {i+1}º lugar: {j.ranking.values()} com {p.ranking.values()}')