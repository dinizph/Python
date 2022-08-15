# pessoa = []
# homem = []
# mulher = []
totalidade = 0
maioridadehomem = 0
m20 = 0
nomevelho = ''
# nome = []
# idade = []
# sexo = []
for c in range(1,5):
    print('----- {}ª pessoa -----'.format(c))
    n = input('Nome: ')
    i = int(input('Idade: '))
    s = input('Sexo como M e F: ').upper().strip()
    # pessoa.append([n,i,s])
    totalidade += i
    if s == 'M' and i > maioridadehomem:
        maioridadehomem = i
        nomevelho = n
        # homem.append([n,i,s])
    if s == 'F' and i <= 20:
        m20 += 1
# print('lista das pessoas',pessoa)
# print('lista dos homens',homem)
# print('lista das mulheres',mulher)
print('-----  -----')
print('Media de idade é {}'.format(float(totalidade/4)))
print('O homem mais velho é {} e tem {}'.format(nomevelho,maioridadehomem))
print('{} mulheres tem menos de 20'.format(m20))
# print('Media de idade: ')
# print(sexo.where('F'))

# primeira tentativa
# for i in range(0,1):
#     n = input('Digite seu nome: ')
#     nome.append(n)
#     i = int(input('Digite sua idade: '))
#     idade.append(i)
#     s = input('Digite seu sexo como M e F: ').upper()
#     sexo.append(s)