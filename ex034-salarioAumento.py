sal = float(input('Digite o seu salario: '))

if sal > 1250:
    sal = sal * 1.1
    print('Novo salário é R$ {:.2f}'.format(sal))
else:
    sal = sal * 1.15
    print('Novo salário é R$ {:.2f}'.format(sal))