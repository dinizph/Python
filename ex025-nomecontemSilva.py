#programa que verifica se um nome tem silva

nome = input('Digite o nome completo: ')
nome = nome.upper()

if 'SILVA' in nome:
    print('Tem Silva')
else:
    print('Nao tem Silva')