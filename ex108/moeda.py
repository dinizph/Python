#aumentar(), diminuir(), dobro() e metade()
#
#
#
def metade(preço=0):
    return preço/2

def dobro(preço=0):
    return  preço * 2

def aumentar(preço=0,i=0):
    return  preço + ( preço * i/100)

def diminuir(preço=0,i=0):
    return  preço - ( preço * i/100)

def moeda(preço = 0, moeda = 'RS '):
    return f'{moeda}{preço:.2f}'.replace('.',',')