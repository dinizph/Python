# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
continuar = ''
while continuar != 'N':
    n = int(input('Digite um numero inteiro: '))
    lista.append(n)
    continuar = input('Deseja CONTINUAR?[S/N]:').strip().upper()[0]
listaInvertida = lista.sort(reverse=True)
print(lista)
print(f'Foram digitados {len(lista)}.')
print(f'A lista em ordem descrescente: {lista}')
print(f'O numero 5 está na lista? {5 in lista}')