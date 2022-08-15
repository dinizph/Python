soma = 0
count = 0
n = 0
menor = n
maior = 0
continua = 'S'

while continua != 'N':
    n = int(input('Digite um numero inteiro: '))
    soma = soma + n
    count += 1
    if count == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continua = str(input('Continuar? [S/N]: ')).upper().strip()

# soma = soma - 999
print('\nValor da soma foi {} de um total de {} numeros somados'.format(soma,count))

media = soma / (count)

print('Voce digitou {} numeros, a media foi {}, o menor foi {} e o maior foi {}'.format(count, media, menor,maior))
