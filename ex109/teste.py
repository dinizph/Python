

from ex109 import moeda

num = float(input('Digite o preço: '))
print(f'A metade de R${num} é {moeda.metade(num, True)}')
print(f'O dobro de R${num} é {moeda.dobro(num, True)}')
print(f'Aumentando em 10% temos {moeda.aumentar(num, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(num, 13, True)}')