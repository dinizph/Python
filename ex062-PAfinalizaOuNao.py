#10 termos de PA usando while

razao = int(input('Digite a razao da PA: '))
termo = int(input('Digite o primeiro termo da PA: '))
t1 = termo
qtermos = 1

while qtermos != 0:
    qtermos = int(input('Quantos termos deseja mostrar?: '))
    while termo < (razao * qtermos + t1):
        print(termo)
        termo += razao
    #qtermos = 1
    termo = termo - (razao * qtermos)
print('\n===Programa finalizado!!!===')
