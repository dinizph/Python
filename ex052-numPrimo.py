n = int(input('Digite um numero inteiro: '))
div = 0

for i in range(1, n + 1):
    if n % i == 0:
        div += 1

if div == 2:
    print('PRIMO')
else:
    print('NÃO É PRIMO foi dividido {} vezes'.format(div))
