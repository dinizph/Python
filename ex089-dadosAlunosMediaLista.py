listaAlunos = []
infoaluno = []
continuar = ' '
while continuar not in 'nN':
    nome = str(input('Nome: '))
    infoaluno.append(nome)
    nota1 = float(input('Nota 1: '))
    infoaluno.append(nota1)
    nota2 = float(input('Nota 2: '))
    infoaluno.append(nota2)
    listaAlunos.append(infoaluno)
    infoaluno = []
    print('=' * 30)
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    print('=' * 30)
print('Nº    Nome      Media')
for i, (nom, not1, not2) in enumerate(listaAlunos):
    num = i
    nome = nom
    anota1 = not1
    anota2 = not2
    print(f'{num}     {nome}       {(anota1+anota2)/2}')
aluno = -1
while aluno != 999:
    aluno = int(input('Notas de qual aluno? (999 finaliza programa):'))
    if aluno == 999:
        print('FINALIZANDO...')
        break
    print(f'Notas de {listaAlunos[aluno][0]} são [{listaAlunos[aluno][1]} e {listaAlunos[aluno][2]}]')
