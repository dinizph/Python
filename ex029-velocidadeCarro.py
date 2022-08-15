velo = int(input('Digite a velocidade: '))

if velo > 80:
    acima = velo - 80
    multa = acima * 7
    print('Voce passou em {} km/h acima da velocidade permitidade e foi multado em R$ {:.2f}'.format(acima, multa))
else:
    print('Velocidade dentro do permitido.')