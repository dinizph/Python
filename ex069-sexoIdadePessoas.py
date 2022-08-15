maior18 = 0
homens = 0
mulher20 = 0
counter = 1
sair = ''

while sair != 'SIM':
    print('----- {}ª pessoa -----'.format(counter))
    n = input('Nome: ')
    i = int(input('Idade: '))
    s = input('Sexo como M e F: ').upper().strip()
    if i >= 18:
        maior18 += 1
    if s == 'M':
        homens += 1
    if s == 'F':
        if i <= 20:
            mulher20 += 1
    counter += 1
    sair = str(input('Deseja SAIR?[SIM/NÃO]: ')).upper().strip()
print('-='*40)
print(f'Foram {maior18} pessoas cadastradas com mais de 18 anos')
print(f'Foram cadastrados {homens} homens')
print(f'Foram {mulher20} mulheres cadastradas com menos de 20')
