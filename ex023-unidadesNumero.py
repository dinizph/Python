#ler numero de zero a 9999 e dizer qts milhares, centenas, dezenas e unidades

num = int(input('Digite um numero entre 0 e 9999: '))

numM = num // 1000
numC = num // 100 % 10
numD = num // 10 % 10
numU = num // 1 % 10



print('Unidades de milhar: ',numM)
print('Centenas: ',str(numC))
print('Dezenas: ',str(numD))
print('Unidades: ',str(numU))
