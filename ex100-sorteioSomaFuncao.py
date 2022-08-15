#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
numeros = []
# sorteia() e somaPar()
#
#sortear 5 inteiros e colocar em uma lista
#
#
def sorteia():
    for i in range(0,5):
        n = randint(1,10)
        numeros.append(n)
    print(f'Os 5 numeros sorteados: {numeros}')
def somaPar(arg):
    soma = 0
    for i in arg:
        if i % 2 == 0:
            soma += i
    print(f'Somando os numeros pares temos um total de: {soma}')

sorteia()
somaPar(numeros)
