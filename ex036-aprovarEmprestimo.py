valor = float(input('Insira valor total da casa: '))
salario = float(input('Qual o valor o seu salario?: '))
anos = int(input('Quantos anos para pagar?: '))

meses = anos * 12
prestacao = valor / meses

if prestacao <= 0.3 * salario:
    print('Emprestimo aprovado, prestaçao será R$ {:.2f} por {} meses'.format(prestacao, meses))
else:
    print('Emprestimo negado, prestaçao será R$ {:.2f} por {} meses'.format(prestacao, meses))