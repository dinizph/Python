ano = int(input('Insira seu ano de nascimento: '))


if 2022 - ano <= 9:
    print('MIRIM')
elif 2022 - ano <= 14:
    print('INFANTIL')
elif 2022 - ano <= 19:
    print('JUNIOR')
elif 2022 - ano <= 20:
    print('SENIOR')
else:
    print('MASTER')
