#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
lista = []

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))
if aluno['Média'] < 5:
    aluno['Situação'] = 'REPROVADO'
else:
    aluno['Situação'] = 'APROVADO'
lista.append(aluno.copy())

print('=-_'*30)

#- Nome é igual a NOME
print(f'Nome é igual a {aluno["Nome"]}')
#- Media é igual a NOTA
print(f'Média é igual a {aluno["Média"]}')
#- Situação é igual a SITUAÇAO
print(f'A situação é igual a {aluno["Situação"]}')

print('=-_'*30)

for k, v in aluno.items():
    print(f' - {k} é igual a {v}')