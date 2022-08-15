peso = float(input('Digite seu peso: '))
h = float(input('Digite sua altura em centimetros: ')) / 100

imc = peso / (h * h)

if imc < 18.5:
    print('IMC de {:.2f}, esta ABAIXO DO PESO'.format(imc))
elif imc < 25:
    print('IMC de {:.2f}, esta com PESO IDEAL'.format(imc))
elif imc < 30:
    print('IMC de {:.2f}, esta com SOBREPESO'.format(imc))
elif imc <= 40:
    print('IMC de {:.2f}, esta com OBESIDADE'.format(imc))
else:
    print('IMC de {:.2f}, esta com OBESIDADE MORBIDA'.format(imc))
