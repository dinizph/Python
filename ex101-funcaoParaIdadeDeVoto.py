#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(arg=0):
    from datetime import datetime
    if arg == 0:
        arg = int(input('Em que ano você nasceu?: '))
    idade =  datetime.now().year - arg
    situ = ''
    if  idade >= 18 or idade < 60:
        situ = 'VOTO OBRIGATORIO'
    if idade >= 16 and idade < 18:
        situ = "VOTO OPCIONAL"
    if idade < 16:
        situ = 'NÃO VOTA'
    print(f'Com {idade} anos: {situ}.')


voto(1991)