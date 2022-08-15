num1 = int(input('Insira o primeiro numero inteiro: '))
num2 = int(input('Insira o segundo numero inteiro: '))

if num1 > num2:
    print('{} é maior'.format(num1))
elif num1 == num2:
    print('Os dois valores são iguais')
else:
    print('{} é maior'.format(num2))