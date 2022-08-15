#qts km e qts dias foi alugado. Calcule o preço a pagar. R$60 diaria e R$0,15 por km rodado

d = float(input('Quantos dias usou o carro? '))
km = float(input('Quantos km rodou? '))

t = (d * 60) + (km * 0.15)

print('O valor total a ser pago é R$ {:.2f}'.format(t))