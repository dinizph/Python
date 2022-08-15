#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
n = 0
# usuario vai digitar 5 valores
# esses valores vao ser armazenados em uma lista
# os novos valores serao inseridos na lista na ordem crescente
for i in range(0,5):
    n = int(input('Digite um numero: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos += 1
print('!-!-'*20)
print('Segue lista: ', end=' ')
print(lista)