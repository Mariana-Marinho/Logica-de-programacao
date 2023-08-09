nomeInimigo = input()
nomeAliado = input()
climaAtual = input()

menor = maior = quantidade = 0

mensagens = list()
mensagem_atual = list()

numero = 0

entrada = input()

while entrada != 'Cansado':

    # contar a quantidade de mensagens digitadas
    quantidade += 1

    for caractere in entrada:

        if caractere == ' ':
            # separar os numeros por espaco
            espaco = entrada.index(caractere)
            numero = int(entrada[:espaco])

            # remover o numero atual da entrada
            entrada = entrada[espaco + 1:]
            # por o numero atual na lista
            mensagem_atual.append(numero)

    # por ultimo numero na lista
    mensagem_atual.append(int(entrada))
    # por a lista da mensagem atual dentro de uma lista com todas as mensagens
    mensagens.append(mensagem_atual)

    # clarear a mensagem atual
    mensagem_atual = []

    entrada = input()

if climaAtual != 'Ensolarado' and climaAtual != 'Nublado' and climaAtual != 'ChuvosoNormal' and climaAtual != 'ChuvosoComRaio':
    print('Infelizmente esse clima não está bom. Não conseguimos decifrar a mensagem, o que será do mundo agora??')
    print(f'Tenho certeza que conseguiremos na próxima {nomeAliado}')

else:
    if climaAtual == 'Ensolarado':
        # funcao para organizar em ordem crescente
        for linha in mensagens:
            # fixa um numero
            for i in range(9):
                # passa por toda a lista
                for j in range(9):
                    # se o numero fixo for menor, troca a posicao
                    if linha[i] < linha[j]:
                        linha[i], linha[j] = linha[j], linha[i]

        print(
            f'Caramba! Finalmente organizamos a mensagem secreta do {nomeInimigo} com esse clima Ensolarado! Vamos nessa {nomeAliado}!')


    elif climaAtual == 'Nublado':
        # funcao para organizar em ordem decrescente
        for linha in mensagens:
            # fixa um numero
            for i in range(9):
                # passa por toda a lista
                for j in range(9):
                    # se o numero fixo for maior, troca a posicao
                    if linha[i] > linha[j]:
                        linha[i], linha[j] = linha[j], linha[i]

        print(
            f'Ufa! Mesmo com o clima Nublado ainda desvendamos a mensagem do {nomeInimigo}! Vamos nessa {nomeAliado}!')


    elif climaAtual == 'ChuvosoNormal':
        for i in range(quantidade - 1):
            for posicao in range(9):

                if mensagens[i][posicao] < mensagens[i + 1][posicao]:
                    mensagens[i][posicao], mensagens[i + 1][posicao] = mensagens[i + 1][posicao], mensagens[i][posicao]

        print(
            f'Nem mesmo a chuva vai nos parar de salvar o mundo! Desvendamos a mensagem do {nomeInimigo}! Vamos nessa {nomeAliado}!')


    elif climaAtual == 'ChuvosoComRaio':
        for i in range(quantidade - 1):
            for posicao in range(9):

                if mensagens[i][posicao] > mensagens[i + 1][posicao]:
                    mensagens[i][posicao], mensagens[i + 1][posicao] = mensagens[i + 1][posicao], mensagens[i][posicao]

        print(
            f'Eitaa! Até mesmo essa chuva com trovoadas não nos parou. Estamos indo até você, {nomeInimigo}! Vamos nessa {nomeAliado}!')

    print(
        f'Agora decodificamos as {quantidade} mensagens do {nomeInimigo} e sabemos seus {quantidade} lugares de ataque.')
    print(f'Os lugares sao:')

    for i in range(quantidade):
        print(f'{i + 1} lugar:')
        print(f"Coordenadas: {mensagens[i][0]}° {mensagens[i][1]}' {mensagens[i][2]}''")
        print(f'Horario: {mensagens[i][3]}h {mensagens[i][4]}m {mensagens[i][5]}s')
        print(f'Data: {mensagens[i][6]}/{mensagens[i][7]}/{mensagens[i][8]}')

    print(f'Vamos rapido {nomeAliado}!!')