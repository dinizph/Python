valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')
# Parte 2 da aula
# =============
# =============
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# print(valores)
# =============
# =============
# a = [2,3,4,8]
# b = a
# As duas listas sao ligadas e quando uma é atualizada a outra tambem é, se eu atualizar um valor em b a lista também é atualizada o valor igual

# Para resolver a copia deve fatiar a primeira lista com o comando [:];
# b = a[:]
# =============
# =============