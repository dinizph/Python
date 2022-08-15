#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def linhas(txt):
    print('~' * (len(txt) + 4))
    print('  '+ str(txt))
    print('~' * (len(txt) + 4))

linhas('')