#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
pessoa = {}
lista = []
continuar = ''
# cadastrar usuários com nome, sexo e idade em um dicionario e inserir o dict em uma list
while True:
    if continuar in ' sS':
        pessoa['nome'] = str(input('Nome: '))
        pessoa['sexo'] = str(input('Sexo: ')).upper().strip()[0]
        # if pessoa['sexo'] not in 'mMfF':
        #     print('Erro! responda com M ou F')
        while pessoa['sexo'] not in 'mMfF':
            print('Erro! responda com M ou F')
            pessoa['sexo'] = str(input('Sexo: ')).upper().strip()[0]
        pessoa['idade'] = int(input('Idade: '))
        lista.append(pessoa.copy())
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        while continuar not in 'sSnN':
            print('ERRO! responda somente com S ou N. ')
            continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
            if  continuar == 'S':
                break
    else:
        break
print('-='*30)
print(lista)
print('-='*30)
#aceitar somente M e F para sexo e somente S e N para continuar ou nao
#A total de pessoas registradas
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
#b media de idade
# media =  float(sum(pessoa["idade"] for pessoa in lista)/len(lista))
# print(media)
print(f'B) A média de idade é {float(sum(pessoa["idade"] for pessoa in lista)/len(lista)):.2f} de anos')
#c lista de mulheres cadastradas
print(f'C) As mulheres cadastradas foram: ',end=' ')
for pessoa in lista:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end='; ')
    # else:
    #     print()
print()
#d lista de pessoas acima da media de idade
print(f'D) Lista de pessoas que estão acima da média de idade:  ')
for pessoa in lista:
    if pessoa['idade'] > float(sum(pessoa["idade"] for pessoa in lista)/len(lista)):
        for i,(k,v) in enumerate(pessoa.items()):
            print(f'    {k} = {v}', end='; ')
        print()
print('-='*30)
print('<<ENCERRADO>>')
