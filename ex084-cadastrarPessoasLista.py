continuar = ''
pessoa = list()
lista = list()
maior = menor = 0
while continuar != 'N':
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        maior = pessoa[1]
        menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('Quer Continuar?: [S/N]')).strip().upper()[0]

print('Maior peso KG',maior)
print('Menor peso KG',menor)

# for i in lista:
#     print(i[1])

print(f'Foram cadastradas {len(lista)} pessoas')
print(lista)
print(f'Maior peso foi {maior} KG e As pessoas mais pesadas foram: ',end=' ')

for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'Menor peso {menor} KG e as pessoas mais leves foram: ', end=' ')

for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')