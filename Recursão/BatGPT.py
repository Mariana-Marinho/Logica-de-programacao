def busca_palavras(matriz, palavra, x, y, pos, visitados):
    ''' procura a letra da palavra na matriz '''

    if pos == len(palavra):
        return True

    if x < 0 or x >= len(matriz) or y < 0 or y >= len(matriz[0]) or (x, y) in visitados:
        return False

    if matriz[x][y] == palavra[pos]:
        visitados.append(matriz[x][y])

        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
            if busca_palavras(matriz, palavra, x + dx, y + dy, pos + 1, visitados):
                return True

        visitados.pop()

    return False


def vilao_achado():
    ''' retorna verdadeiro se algum vilão foi achado '''

    viloes = ['ARLEQUINA', 'PINGUIM', 'JOKER', 'ESPANTALHO', 'DUASCARAS', 'REIDOSCONDIMENTOS', 'CHARADA']
    n = int(input())

    m = []
    linha = []

    for i in range(n):
        entrada = input()
        for letra in entrada:
            if letra != ' ':
                linha.append(letra)
        m.append(linha)
        linha = []

    for vilao in viloes:
        for i in range(n):
            for j in range(n):
                if busca_palavras(m, vilao, i, j, 0, []):
                    if vilao == 'CHARADA':
                        print("Isso!!! Encontramos uma pista, mas somente o Charada está envolvido.")
                    else:
                        print(f"Isso!!! Encontramos uma pista, {vilao.title()} está junto com o Charada.")

                    return True

    return False


if not vilao_achado():
    print("Poxa... acho que seguimos uma pista falsa.")
