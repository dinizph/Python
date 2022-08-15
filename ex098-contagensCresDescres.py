#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep
def contagem():
    print('-='*30)
    print('Contagem de 1 a 10:')
    for i in range(1,11,1):
        print(i, end='  ')
        sleep(0.25)
    print('FIM!')
    sleep(0.25)
    print('-=' * 30)
    print('Contagem de 10 a 0:')
    for i in range(10,-1,-2):
        print(i, end='  ')
        sleep(0.25)
    print('FIM!')
    sleep(0.25)
    print('-=' * 30)
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    razao = int(input('Razao: '))
    if razao == 0:
        while razao == 0:
            print('Razao não pode ser 0!!!')
            razao = int(input('Razao: '))
    if fim < inicio:
        while razao > 0:
            print('Razão deve ser negativa')
            razao = int(input('Razao: '))
    for i in range(inicio, fim+1, razao):
        print(i, end='  ')
        sleep(0.25)
    print('FIM!')
    sleep(0.25)
    print()

contagem()

