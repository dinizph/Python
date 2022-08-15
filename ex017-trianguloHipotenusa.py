#ler os lados e dar a hipotenusa

l1 = float(input('Insira lado 1: '))
l2 = float(input('Insira lado 2: '))

hip = (l1 ** 2 + l2 ** 2) ** float(1/2)

print('Hipotenusa é : {:.2f}'.format(hip))