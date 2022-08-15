razao = int(input('Digite a razao da PA: '))
termo = int(input('Digite o primeiro termo da PA: '))

print(termo)
for i in range(0,9):
    termo += razao
    print(termo)
print('==FIM==')