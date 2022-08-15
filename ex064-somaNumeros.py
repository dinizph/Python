soma = 0
count = 0
n = 0

while n != 999:
    n = int(input('Digite um numero inteiro: '))
    soma = soma + n
    count += 1

soma = soma - 999
print('\nValor da soma foi {} de um total de {} numeros somados'.format(soma,count-1))
