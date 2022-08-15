ano = int(input('Insira seu ano de nascimento: '))


if 2022 - ano < 18:
    falta = 18 - (2022 - ano)
    print('Ainda vai se alistar faltam {} anos'.format(falta))

elif 2022 - ano == 18:
    print('Está no tempo de se alistar')
else:
    falta = (18 - (2022 - ano)) * -1
    print('Já passou do tempo de se alistar em {} anos'.format(falta))