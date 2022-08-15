n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('A media foi {} e está REPROVADO'.format(media))
elif media >= 5 and media <= 6.9:
    print('A media foi {} e está em RECUPERAÇÃO'.format(media))
else:
    print('A media foi {} e está APROVADO'.format(media))