soma = 0
count = 0
n = 0

while True:
    n = int(input('Digite um numero inteiro: '))
    if n == 999:
        break
    soma = soma + n
    count += 1

print('\nValor da soma foi {} de um total de {} numeros somados'.format(soma,count))