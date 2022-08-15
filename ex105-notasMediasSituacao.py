
def notas(*n, sit=False):
    """
    funcao para nalisar notas e situacoes de varios alunos.
    :param n: aceita varias notas
    :param sit: verica a situacao do aluno baseado na media
    :return:
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r



#retornar dicionario com
#– Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)
resp = notas(5,6,7,sit=True)
print(resp)