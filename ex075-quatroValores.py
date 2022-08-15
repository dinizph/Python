lista = []
lista.append(int(input('Digite um numero: ')))
lista.append(int(input('Digite um numero: ')))
lista.append(int(input('Digite um numero: ')))
lista.append(int(input('Digite um numero: ')))
print(type(lista))
print(lista)
lista = tuple(lista)
print(lista)

count = lista.count(9)
print('Vezes que o número 9 apareceu: ',count)

count3 = lista.count(3)
if  count3 > 0:
    pos3 = lista.index(3)
    print('Posição que o número 3 apareceu: ',pos3)
else:
    print('O número 3 NÃO APARECEU')

print('Os números pares foram: ', end=' ')
for i in lista:
    if (i % 2 == 0):
        print(i, end=' ')


