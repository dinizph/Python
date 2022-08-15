#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
pessoa = {}
lista = []
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Nascimento'] = int(input('Ano de Nascimento: '))
    pessoa['CarteiraTrabalho'] = int(input('Numero da Carteira de Trabalho (0 se não tem): '))
    if pessoa['CarteiraTrabalho'] == 0:
        break
    pessoa['AnoContratado'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Aposentadoria'] = (datetime.now().year - pessoa['Nascimento']) + 35 - pessoa['AnoContratado']
    lista.append(pessoa.copy())
    break
print('=-_'*30)
print(lista)
if len(pessoa) >= 4:
    print('Nome', pessoa['Nome'])
    print('Idade é: ', datetime.now().year - (pessoa['Nascimento']))
    print('Nº Carteira', pessoa['CarteiraTrabalho'])
    print('Ano de aposentadoria será: ', pessoa['AnoContratado']+35)
    print('Salario: R$', pessoa['Salário'])
else:
    print('Nome', pessoa['Nome'])
    print('Idade é: ', datetime.now().year - (pessoa['Nascimento']))
    print('Não possui carteira de trabalho')
