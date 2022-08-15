#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o  nome santo

nome = input('Digite o nome de uma cidade: ').strip()

# nome = nome.split()
# print('O primeiro nome tem {} letras '.format(len(nome[0])))

nome = nome.split()
nome = nome[0]
nome = nome.upper()


if nome == 'SANTO':
    print('\n Nome da cidade começa com Santo? \n \n Sim')
else:
    print('\n Nome da cidade começa com Santo? \n \n Nao')


#reposta:
# ===============
# cid = str(input('Cidade: ')).strip()
# print(cid[:5].upper() == 'SANTO')
# ===============
#cid[:5] testa se os primeiros 5 caracteres sao santo e retorna true ou false



