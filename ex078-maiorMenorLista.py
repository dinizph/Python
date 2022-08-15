
# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

lista = []
maior = 0
menor = 0

for i in range(0,5):
    lista.append(int(input('Digite um número: ')))
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    else:
        if lista[i] < menor:
            menor = lista[i]
        if lista[i] > maior:
            maior = lista[i]

print('Voce digitiou: ',sorted(lista))
print(f'Maior valor foi {maior} na posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}..>', end=' ')
print()
print(f'Menor valor foi {menor} na posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}..>', end=' ')

