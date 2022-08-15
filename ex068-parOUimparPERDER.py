from random import randint
choice = ''
i = 1
sort = ''
count = 0

while True:
    num = randint(0,100)
    choice = str(input('Par ou Impar? [P/I]: ')).strip().upper()
    print(f'numero sorteado {num}\nescolha do jogador {choice}')

    if num % 2 == 0:
        sort = 'P'
        if choice == sort:
            print(f'Deu {sort} voce ganhou!')
            count += 1
        if choice != sort:
            print(f'Deu {sort}, e voce escolheu1 {choice}')
            break
    else:
        sort = 'I'
        if choice == sort:
            print(f'Perdeu deu {sort} voce ganhou!')
            count += 1

        if choice != sort:
            # sort = 'I'
            print(f'Perdeu, deu {sort}, e voce escolheu {choice}')
            break
print('='*30)
print(f'Jogador ganhou {count} vezes')