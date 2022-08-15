from datetime import date

atual = date.today().year
maior = 0
for i in range(0, 7):

    nasc = int(input('Ano de nascimento: '))
    #idade = atual - nasc
    if atual - nasc >= 18:
        maior += 1
menor = 7 - maior

print('{} pessoas são MAIORES e {} são menores'.format(maior,menor))



