

num = int(input('Digite um numero inteiro: '))

base = int(input('Digite\n \n 1 para binario \n 2 para octal \n 3 para hexadecimal\n \nInsira sua opção de base a seguir: '))

if base == 1:
    print('O valor binário é {}'.format(bin(num)))
elif base == 2:
    print('O valor octal é {}'.format(oct(num)))
elif base == 3:
    print('O valor hexadecimal é {}'.format(hex(num)))
else:
    print('Digite um dos 3 valores válidos!')