expr = str(input('Digite a expressão: '))
abre = []

for simbolo in expr:
    if simbolo == '(':
        abre.append(simbolo)
    elif simbolo == ')':
        abre.pop()
    # else:
    #     if len(abre) == 0:
    #         print('Expressão está correta')
    #     else:
    #         print('Expressao invalida')
if len(abre) == 0:
    print('Expressao valida')
else:
    print('Expressao invalida')

