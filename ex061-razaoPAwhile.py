#10 termos de PA usando while

razao = int(input('Digite a razao da PA: '))
termo = int(input('Digite o primeiro termo da PA: '))
t1 = termo
qtermos = 10

while termo < (razao * qtermos + t1):
    print(termo)
    termo += razao
#
#
#
#
# razao = int(input('Digite a razao da PA: '))
# termo = int(input('Digite o primeiro termo da PA: '))
#
# print(termo)
# for i in range(0,9):
#     termo += razao
#     print(termo)
# print('==FIM==')