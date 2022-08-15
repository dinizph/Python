#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

info = {}
gols = []
cod = 0
jogadores = []
while True:
    gols = []
    info['nome'] = str(input('Nome do jogador: '))
    info['partidas'] = int(input(f'Quantas partidas {info["nome"]} jogou: '))
    for i in range(0,info['partidas']):
        g = int(input(f'Quantos gols fez na partida {i}: '))
        gols.append(g)
    info['gols'] = gols
    info['total'] = sum(gols)
    info['cod'] = cod
    cod += 1
    jogadores.append(info.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if  resp in 'SN':
            break
    if resp == 'N':
        break
print(('-='*30))
# print o diocionario completo
print(jogadores)
print(('-='*30))
#exibir tabela com infos dos jogadores:
print(f'Cod. Nome         Gols         Total')
print('-'*30)
for info in jogadores:

        print(info["cod"], end=' ')
        print(info["nome"], end=' ')
        print(info["gols"], end=' ')
        print(info["total"], end=' ')
        print()
print(('-='*30))
#verificar codigo do jogador e mostrar informaçoes
while True:
    codigo = int(input('Mostrar dados de qual jogador? (999 para a consulta): '))
    if codigo == 999:
        break
    if codigo >= len(jogadores):
        print(f'ERRO, nao existe jogador com o codigo {codigo}')
    else:
        print('-- LEVANTAMENTO DO JOGADOR ',jogadores[codigo]["nome"])
        for i, g in enumerate(jogadores[codigo]["gols"]):
            print(f'    No jogo {i} fez {g} gols.')
        print('-='*30)
        # print(f'    => Na partida {i+1}, fez {v} gols.')



#enumerate com nome do jogador, gol e total de gols
# for i, (k, v) in enumerate(info.items()):
#     print(f'O campo {k} tem o valor {v}')
# enumerate das partidas e gols feitos no dia e no final o total de gol em todas as partidas
# print(f'O jogador {info["nome"]} jogous {info["partidas"]} partidas.')
# print(f'Foi um total de {info["total"]} gols.')