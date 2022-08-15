#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

#nome do jogador
# n de partidas q jogou
# n de gols na partiga n e depois n+1
info = {}
gols = []
info['nome'] = str(input('Nome do jogador: '))
info['partidas'] = int(input(f'Quantas partidas {info["nome"]} jogou:'))

for i in range(0,info['partidas']):
    g = int(input(f'Quantos gols fez na partida {i}: '))
    gols.append(g)
info['gols'] = gols
info['total'] = sum(gols)
print(('-='*30))
# print o diocionario completo
print(info)
print(('-='*30))
#enumerate com nome do jogador, gol e total de gols
for i, (k, v) in enumerate(info.items()):
    print(f'O campo {k} tem o valor {v}')
print(('-='*30))
# enumerate das partidas e gols feitos no dia e no final o total de gol em todas as partidas
print(f'O jogador {info["nome"]} jogous {info["partidas"]} partidas.')
for i, v in enumerate(gols):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {info["total"]} gols.')
