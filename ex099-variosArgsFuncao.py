#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*args):
    print('-='*20)
    for i in args:
        print(i, end=' ')
    print(f'Foram digitados {len(args)} argumentos.')
    if len(args) != 0:
        print(f'O maior deles é {max(args)}')
    else:
        print(f'O maior deles é 0')



maior(1,2,3,9,5,6,7)
maior(5)
maior()