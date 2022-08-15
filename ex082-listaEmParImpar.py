par = []
impar = []
continuar = ''
while continuar != 'N':
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = input('Deseja CONTINUAR?[S/N]:').strip().upper()[0]

lista = par + impar
print(lista)
print(f'Numeros pares {par}.')
print(f'A lista impares: {impar}')