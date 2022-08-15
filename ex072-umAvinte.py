n = 0
while 0 <= n <= 20:
    numeros = ("zero","um", "dois", "três", "quatro","cinco", "seis", "sete", "oito", "nove","dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove","vinte")
    n = int(input('Digite um numero entre 0 e 20: '))
    if n < 0 or n > 20:
        break
    print('Voce escolheu o numero',numeros[n])

print('programa finalizado numero invalido!!!')