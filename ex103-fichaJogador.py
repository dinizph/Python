#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(j=0,g=0):
    if j == 0:
        j = input('Nome do jogador: ')
    if g == 0:
        g = input('Quantidade de gols: ')
        if g == '':
            g = '0'
    print(f'O jogador {j} fez {g} gols no campeonato.')

ficha()