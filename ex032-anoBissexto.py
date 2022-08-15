ano = int(input('Digite o ano: '))
#and ano % 100 != 0
#and ano % 400 == 0

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('Ano bissexto')
        else:
            print('Ano não é bissexto')
    else:
        print('Ano bissexto')
else:
    print('Ano não é bissexto')