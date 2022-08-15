lista = []
continuar = ''
n = -1

while continuar != 'N':
    n = int(input('Digite um numero111: '))
    if n in lista:
        print('Numero Duplicado, digite outro numero: ')
    while n in lista:
        n = int(input('Digite um numero222: '))
        if n in lista:
            print('Numero Duplicado, digite outro numero222: ')
        else:
            break
    lista.append(n)
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]

print('Voce digitou: ',sorted(lista))
