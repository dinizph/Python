preco = float(input('Digite o preço do produto: '))

condicao = int(input('Digite a opção equivalente a opção da condição de pagamento:\n \n1 - A vista dinheiro/cheque com 10% de desconto.\n2 - A vista no cartao com 5% de desconto.\n3 - 2x no cartao preço normal sem desconto.\n4 - 3x ou mais com 20% de juros no valor do produto.\n\nDigite o numero da opção: '))

if condicao == 1:
    preco = preco * 0.9
    print('O valor a ser pago será de R$ {:.2f}'.format(preco))
elif condicao == 2:
    preco = preco * 0.95
    print('O valor a ser pago será de R$ {:.2f}'.format(preco))
elif condicao == 3:
    preco = preco
    print('O valor a ser pago será de R$ {:.2f}'.format(preco))
else:
    preco = preco * 1.2
    print('O valor a ser pago será de R$ {:.2f}'.format(preco))
