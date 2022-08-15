lista = []
soma = 0
for i in range(0,6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        lista.append(n)
        soma += n

print('Lista dos numeros validos ', lista)
print('Soma dos numeros validos ', soma)
