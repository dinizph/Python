num1 = int(input('1- Digite um numero: '))
num2 = int(input('2- Digite um numero: '))
num3 = int(input('3- Digite um numero: '))

if num1 > num2:
    if num1 > num3:
        print('O {} é o maior'.format(num1))
else:
    if  num2 > num3:
        print('O {} é o maior'.format(num2))
    else:
        print('O {} é o maior'.format(num3))
    

