#pegar frase e dizer quantas vezes tem a letra A, qual a posicao dela na primeira vez e que posicao aparece por ultimo

frase = input('Digite uma frase: ').strip()
#deixar tudo maiusculo para depois contar
frase = frase.upper()
fraseA = frase.count('A')
letra = 'A'

print('A letra A aparece {}'.format(fraseA))
print('A letra A aparece na posiçao {}'.format(frase.index(letra)))

A = 'A'
index = frase.rfind(A)

if index != -1:
    print('A letra {} é achada pela ultima vez na posiçao {}'.format(A,index))
else:
    print('Nao encontrada a letra A')


#resposta usar find()+1 e rfind()+1. rfind é right find