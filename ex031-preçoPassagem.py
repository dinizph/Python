dist = float(input('Digite a distancia da viagem: '))

if dist <= 200:
    valor = dist * 0.5
    print('Valor da passagem é R$ {:.2f}'.format(valor))
else:
    valor = dist * 0.45
    print('Valor da passagem é R$ {:.2f}'.format(valor))