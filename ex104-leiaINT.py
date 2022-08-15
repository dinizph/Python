#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    n = ' '
    while n.isnumeric() == False:
        n = str(input(msg))
        if n.isnumeric() == False:
            print('Número inválido digite um numero inteiro: ')
        else:
            print('Voce acabou de digitar o numero: ',n)
            return int(n)


leiaInt('Digite um numero inteiro: ')
