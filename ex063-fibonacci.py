#mostrar n digitos da sequencia de fibonacci

n = int(input('\nDigite quantas casas da sequencia de fibonacci a ser exibida: '))
start = 0
fib = 0
anter = 0

while n != 0:
    if start == 0:
        print(start)
        start += 1
        fib = start

    else:
        fib = fib + anter
        anter = fib - anter
    n -= 1
    print('{} '.format(fib))