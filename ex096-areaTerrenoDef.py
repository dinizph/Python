#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

#mostrar Controle de terrenos
print('Controle de Terrrenos')
print('='*30)
#pedir largura
def area():
    l = float(input('Largura (m): '))
    c = float(input('Comprimento (m): '))
    print(f'A área de um terreno de {l} x {c} é de {l*c}m²')
    print('=' * 30)
area()

#pedir comprimento
#mostrar L*C é de A
