def classificacao(energia, controle, precisao):
    # classifica a motosserra e retorna a classificacao
    frase = ''
    if energia >= 750 and controle >= 7 and precisao >= 8:
        frase = 'Motosserra Suprema'
    elif energia >= 500 and controle >= 6 and precisao >= 6:
        frase = 'Motosserra Avançada'
    else:
        frase = 'Motosserra Normal'
    return frase


def resultado(inimigo, denji, nome_vilao):
    # retorna o resultado da rodada
    frase = ''
    if denji > inimigo:
        print(f'Denji saiu vitorioso nessa batalha contra o {nome_vilao}')
        frase = 'Vitoria'
    elif inimigo > denji:
        print(f'Denji não conseguiu força o suficiente para derrotar o {nome_vilao}')
        frase = 'Derrota'
    else:
        print(f'Como pode ser possível?? Denji possui a mesma força que o {nome_vilao}')
        frase = 'Empate'
    return frase


def imprimir_resultados(mot, res):
    # printa o resultado depois das 3 rodadas e nao retorna nada
    vitorias = derrotas = empates = 0
    for i in range(3):
        print(f'Rodada {i+1}: {mot[i]} - {res[i]}')
        if res[i] == 'Vitoria':
            vitorias += 1
        elif res[i] == 'Empate':
            empates += 1
        else:
            derrotas += 1

    if vitorias == 3:
        print('Nenhum dos 3 inimigos foram capazes de derrotar o Denji!')

    elif derrotas == 3:
        print('Hoje não foi um dia bom para o Denji, perdeu todas as batalhas')

    elif vitorias == derrotas == empates == 1:
        print('Hoje foi um dia equilibrado para o Denji, conseguiu ganhar, perder e empatar')

    elif vitorias > derrotas and vitorias > empates:
        print('Denji conseguiu derrotar a maioria de seus inimigos')

    elif derrotas > vitorias and derrotas > empates:
        print('Dia péssimo para o Denji, perdeu a maioria de suas batalhas')

    else:
        print('Dia duro para o Denji, empatou de mais')


viloes = ['Makima', 'Reze', 'Santa Claus']
historico_motosseras = []
historico_resultados = []

for x in range(3):
    vilao = viloes[x]
    e = int(input())
    c = int(input())
    p = int(input())
    forca_inimigo = int(input())
    forca_denji = e + (c * p)

    motosserra = classificacao(e, c, p)
    print(f'### Rodada {x + 1} - {vilao} ###')
    print(f'O Denji ira se transformar na {motosserra} para enfrentar o {vilao}')

    historico_motosseras.append(motosserra)
    r = resultado(forca_inimigo, forca_denji, vilao)
    historico_resultados.append(r)

print('### Resultado Final ###')
imprimir_resultados(historico_motosseras, historico_resultados)
