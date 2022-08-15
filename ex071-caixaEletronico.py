valor = 1
q50 = 0
q20 = 0
q10 = 0
q1 = 0
cedulas = 0
qtCedulas = 0

while valor > 0:
    valor = int(input('Digite o valor inteiro a ser sacado: '))
    q50 = valor // 50
    valor = valor - (q50 * 50)
    q20 = valor // 20
    valor = valor - (q20 * 20)
    q10 = valor // 10
    valor = valor - (q10 * 10)
    q1 = valor // 1
    valor = valor - (q1 * 1)
print(f'Foram sacadas {q50} notas de R$ 50')
print(f'Foram sacadas {q20} notas de R$ 20')
print(f'Foram sacadas {q10} notas de R$ 10')
print(f'Foram sacadas {q1} notas de R$ 1')