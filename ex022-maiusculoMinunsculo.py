#Ler nome completo e imprimir: nome com tudo maiusculo, minusculo, quantas letras ao todo sem contar espaços, quantas letras só no primeiro nome

nome = input('Digite o nome completo: ').strip()

print(nome.upper())
#print('\n')
print(nome.lower())
#print('\n')
print('O nome completo tem {} letras '.format(len(nome)))
nome = nome.split()
print('O primeiro nome tem {} letras '.format(len(nome[0])))