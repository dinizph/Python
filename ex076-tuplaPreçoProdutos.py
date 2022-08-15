# Nao deu pra fazer esse, copiei a resposta

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

compras = ('Pão', 8.00,
           'Manteiga', 12.00,
           'Presunto', 10.00,
           'Queijo', 11.00,
           'Café', 20.00,
           'Leite', 5.00)

for i in range(len(compras)):
    if i % 2 == 0:
        print(f'{compras[i]:.<30}', end='')
    else:
        print(f'R${compras[i]:>7.2f}')

print('-'*40)