n = input('Digite uma frese: ')
n = n.strip().upper().replace(" ","")
l = len(n)
print(n)
#print('invertida', end="  ==> ")
nn = n[::-1]
print(nn, end="  ==>  ")
print(n)
if n == nn:
    print('\nÉ palindromo')
else:
    print('\nNÃO é palindromo')
