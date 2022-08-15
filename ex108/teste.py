
from ex108 import moeda

num = float(input('Digite o preço: '))
print(f'A metade de R${num} é R${moeda.moeda(moeda.metade(num))}')
print(f'O dobro de R${num} é R${moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando em 10% temos R${moeda.moeda(moeda.aumentar(num, 10))}')