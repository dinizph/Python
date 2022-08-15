v1 = int(input('Digite um número inteiro: '))
v2 = int(input('Digite outro número inteiro: '))
opcao = 0

while opcao != 5:
    print('''\nESCOLHA UMA DAS OPÇÕES\n
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('\nDigite sua opção: '))
    if opcao == 1:
        print('A soma dos valores escolhidos é: {}'.format(v1+v2))
    elif opcao == 2:
        print('A multiplicação dos valores escolhidos é: {}'.format(v1 * v2))
    elif opcao == 3:
        if v1 > v2:
            print('O numero {} é maior'.format(v1))
        elif    v2 > v1:
            print('O numero {} é maior'.format(v2))
        else:
            print('Os numeros são iguais')
    elif opcao == 4:
        v1 = int(input('Digite um número inteiro: '))
        v2 = int(input('Digite outro número inteiro: '))
    elif opcao == 5:
        break
    else:
        print('Opçao invalida')