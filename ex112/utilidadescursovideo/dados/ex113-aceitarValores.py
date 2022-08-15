while True:
    try:
        n = int(input('Digite uma numero inteiro: '))
        n2 = float(input('Digite um numero real: '))

    except (ValueError, TypeError):
        print('Digite um número valido!')

    else:
        print('-='*20)
        print(f'O inteiro é {n} e o real é {n2}')
        break