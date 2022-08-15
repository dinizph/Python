matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = 0
maiorlinha2 = 0
col3 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor [{l},{c}] na matriz: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if matriz[l][2]:
            col3 += matriz[l][2]
        if matriz[1][c]:
            if matriz[1][c] >= maiorlinha2:
                maiorlinha2 = matriz[1][c]
print('-='*30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^7}]', end=' ')
    print()
print(matriz)
print('Pares total: ', par)
print('Soma Terceira coluna: ',col3)
print('Maior Valor linha 2: ',maiorlinha2)