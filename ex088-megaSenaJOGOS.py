import random
import time
randomlist = []

jogos = int(input('Quantos jogos gerar?: '))
for j in range(0,jogos):
    for i in range(0,6):
        n = random.randint(1,61)
        while n in randomlist:
            n = random.randint(0,61)
        randomlist.append(n)

    print(f'Jogo {j+1}: {sorted(randomlist)}')
    randomlist = []
    time.sleep(1)