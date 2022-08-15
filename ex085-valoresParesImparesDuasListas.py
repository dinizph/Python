# inserir os 7 valores em uma unica lista
# os valores serao separados em duas listas dentro da lista entre par e impar
# mostrar os valores em par e impar em ordem crescente
# ========================================================================================
# ========================================================================================
#soluçao guanabara:
lista = [[], []]
n = 0

for i in range(1,8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print(lista)
print(lista[0])
print(lista[1])
print(sorted(lista[0]))
print(sorted(lista[1]))



# ========================================================================================
# ========================================================================================

# MINHA SOLUÇÃO
# lista = []
# par = []
# impar = []
#
# for i in range(0,7):
#     n = int(input(f'Digite o {i+1}º valor inteiro: '))
#     if n % 2 == 0:
#         par.append(n)
#     else:
#         impar.append(n)
# lista.append(par)
# lista.append(impar)
#
# print(lista)
# print('Valores pares digitados: ', end=' ')
# print(sorted(par))
# print('Valores impares digitados: ', end=' ')
# print(sorted(impar))