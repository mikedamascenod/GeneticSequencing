import os
# input
# ---aaattcc---cccc--
# aactgtgactgcatgcatgactgactg
# Output
# aaattcc---cccc
# tgtgactgcatgcatgactgac


def contar_no_comeco(sequencia):
    tracos = 0
    for c in sequencia:
        if c == '-':
            tracos = tracos + 1
        else:
            break
    return tracos


def contar_no_final(sequencia):
    return contar_no_comeco(reversed(sequencia))


def editar_sequencias(seq1, seq2):
    _inicio = contar_no_comeco(seq1)
    _final = contar_no_final(seq1)

    return(seq1[_inicio:-_final if _final != 0 else len(seq1)],
           seq2[_inicio:-_final if _final != 0 else len(seq2)])


seq1 = '-----aaattcc---cccc--'
seq2 = 'aactgtgactgcatgcatgactgactg'

i = contar_no_comeco(seq1)
f = contar_no_final(seq1)

print(seq1[i:-f])
print(seq2[i:-f])

with open('input/DENV1-X-gb_A75711.fasta.aln') as fasta:
    conteudo = fasta.read()
    linhas = conteudo.split('\n')
    print(linhas)
    cabecalho1 = linhas[0]
    indice = 0
    for l in linhas:
        if '>gb' in l:
            break
        indice = indice + 1

    cabecalho2 = linhas[indice]
    sequencia1 = ''.join(linhas[1:indice])
    sequencia2 = ''.join(linhas[indice+1:])

    with open(os.path.join('output', 'resultado.fasta'), 'w') as res:

        editada1, editada2 = editar_sequencias(sequencia1, sequencia2)

        res.write(cabecalho1 + '\n')
        res.write(editada1 + '\n')
        res.write(cabecalho2 + '\n')
        res.write(editada2)
