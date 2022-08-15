
import random

mao = str(input('Digite pedra, papel ou tesoura: ')).lower()


jokenpo = ['pedra', 'papel', 'tesoura']
#numSort = random.randint(0, len(aluno)-1)
jokenpo = random.choice(jokenpo)

if mao == 'pedra':
    if jokenpo == 'tesoura':
        print('{} - Você GANHOU'.format(jokenpo))
    elif jokenpo == 'papel':
        print('{} - Você PERDEU'.format(jokenpo))
    else:
        print('{} - EMPATE'.format(jokenpo))

elif mao == 'papel':
    if jokenpo == 'pedra':
        print('{} - Você GANHOU'.format(jokenpo))
    elif jokenpo == 'tesoura':
        print('{} - Você PERDEU'.format(jokenpo))
    else:
        print('{} - EMPATE'.format(jokenpo))
elif mao == 'tesoura':
    if jokenpo == 'papel':
        print('{} - Você GANHOU'.format(jokenpo))
    elif jokenpo == 'pedra':
        print('{} - Você PERDEU'.format(jokenpo))
    else:
        print('{} - EMPATE'.format(jokenpo))
else:
    print('Opção inválida')