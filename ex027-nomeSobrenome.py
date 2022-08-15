#ler o nome completo e mostar somente nome e sobrenome

full = input('Digite seu nome completo: ')

nomes = full.split()
first = nomes[0]
last = nomes[-1]

print('Primeiro nome: ',first)
print('Segundo nome: ',last)