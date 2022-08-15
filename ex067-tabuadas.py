n = 0
i = 1

while True:
    n = int(input('Digite um numero de 1 a 10: '))
    if  n < 0:
        break
    while i != 11:
        print(f'{n} x {i} = {n * i}')
        i += 1
    print('-='*20)
    i = 1

print('\nPROGRAMA FINALIZADO')
#
#
# while i <= 10:
#     n = int(input('Digite um numero de 1 a 10: '))
#     print(f'{n} x {i} = {n * i}')
#     i += 1
#     if n <= 0:
#         break

#
# for i in range(1,11):
#     print('{} x {} = {}'.format(n, i, n * i))