continuar = ''
total = 0
barato = ''
count = 0
mil = 0
maior = 0
menor = 0

while continuar != 'N':
    nome = input('Digite o nome do produto: ').upper().strip()
    preco = float(input('Digite o preço: '))
    total = total + preco
    count += 1
    if preco >= 1000:
        mil += 1
    if count == 1:
        barato = nome
        maior = preco
        menor = preco
    else:
        if preco > maior:
            maior = preco
        if preco < menor:
            menor = preco
            barato = nome
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
print(f'Total gasto foi R$ {total:.2f}')
print(f'{mil} produtos custaram acima de R$ 1000,00')
print(f'O {barato} foi o produto mais barato.')