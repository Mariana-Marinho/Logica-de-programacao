def soma_letras(palavra):
    # soma dos valores ascii do nome do demonio, retorna a soma
    soma = 0
    for letra in range(len(palavra)):
        soma += ord(palavra[letra])
    return soma


def cela_vazia(valor, lista):
    # checa se a cela está ou não ocupada
    if valor in lista:
        return False
    else:
        lista.append(valor)
        return True


def proxima_cela(numero_cela, lista_nomes):
    # retorna o novo indice em que o nome deve estar
    for i in range(numero_cela + 1, len(lista_nomes)):
        # se tiver alguma posicao vazia a direita, retorna o index
        if lista_nomes[i] == '':
            return i

    for i in range(numero_cela):
        # se não tiver posicao vazia a direita, le a lista desde o comeco
        if lista_nomes[i] == '':
            return i


def lista_cheia(lista_nomes):
    # checa se a lista esta toda preenchida
    for nome in lista_nomes:
        if nome == '':
            return False
    return True


def alocar(numero_cela, nome, lista_nomes):
    # preenche a lista de nomes a partir da lista de celas
    if lista_nomes[numero_cela] == '':
        lista_nomes[numero_cela] = nome
    else:
        # ve se a lista esta cheia
        if lista_cheia(lista_nomes):
            print('CHEIO')
        # ve se o item da lista a partir do numero da cela esta vazio, se sim, poe o nome
        else:
            i = proxima_cela(numero_cela, lista_nomes)
            lista_nomes[i] = nome


def tirar(nome, lista_nomes):
    # retira o nome da lista de nomes e de celas se existirr e se não tiver imprime a frase correspondente
    if nome in lista_nomes:
        i = lista_nomes.index(nome)
        lista_nomes[i] = ''
    else:
        print('NAO EXISTE')


def imprimir(lista):
    # imprime o nome dos demonios
    nomes = []
    # preenche uma lista so com os nomes
    for demonio in lista:
        if demonio != '':
            nomes.append(demonio)
    # printa os nomes divididos por um espaco
    for i, n in enumerate(nomes):
        if i == 0:
            print(n, end='')
        else:
            print(f' {n}', end='')


demonios = []
entrada = input()
quant_celas = int(entrada[:(entrada.index(' '))])
quant_ordem = int(entrada[(entrada.index(' ')) + 1:])

for i in range(quant_celas):
    demonios.append('')

for i in range(quant_ordem):
    entrada = input()
    ordem = entrada[:(entrada.index(' '))]
    nome_demonio = entrada[(entrada.index(' ')) + 1:]

    indice = soma_letras(nome_demonio) % quant_celas
    if ordem == 'ADICIONAR':
        alocar(indice, nome_demonio, demonios)
    else:
        tirar(nome_demonio, demonios)

imprimir(demonios)