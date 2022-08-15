l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
a = l * h
t = a / 2
print('Sua parede tem {} metros quadrados voce precisa de {:.2f} litros de tinta'.format(a, t))