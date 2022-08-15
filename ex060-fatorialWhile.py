n = int(input('Digite um numero inteiro: '))
i = n
while i > 1:
    i -= 1
    n = n * i

print('\nO fatorial é:',n)