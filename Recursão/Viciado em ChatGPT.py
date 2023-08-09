def traduzir(frase):
    # retorna a mensagem do usuário comprimida
    c = 0
    for i in range(len(frase)):
        if frase[0] == frase[i]:
            c += 1

        else:
            return f'{c}{frase[0]}' + traduzir(frase[c:])
    return f'{c}{frase[0]}'


def somar_digitos(frase, soma=0):
    # retorna a soma dos digitos da frase
    if frase[0].isnumeric():
        soma += int(frase[0])

    if len(frase) == 1:
        return soma
    else:
        return somar_digitos(frase[1:], soma)


def comprimir(soma):
    # retorna a resposta do chatGPT a partir da soma dos digitos da frase
    if 0 < soma <= 5:
        return '1t3a1 1f1a1c3i1n1h1o1 1n3e'
    elif 6 < soma <= 20:
        return '1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o'
    elif 21 < soma <= 30:
        return '1s6o1 1n1a1 1v1i1d2a1 1m4a1n1s3a'
    elif 31 < soma <= 40:
        return '1v5a1 1e2s1t4u3d3a3r1 1r1a1p3a3z'
    else:
        # 40 < soma
        return '3e1s1t5u1d1a1 1n2a1o1 1p1r3a1 1t2u1 1v4e1r'


def descomprimir(frase, resposta=''):
    # retorna a frase descomprimida
    for i in range(int(frase[0])):
        resposta += frase[1]
    if len(frase) == 2:
        return resposta
    else:
        return descomprimir(frase[2:], resposta)


entrada = input()
s = 0
mensagem = ''

while entrada != 'Preciso parar de usar o ChatGPT':
    if entrada == 'Vou pedir ajuda pro meu amigo ChatGPT':
        entrada = input()

        while entrada != 'Não tô entendendo nada':
            s += somar_digitos(entrada)
            usuario = traduzir(entrada)
            chat_gpt = comprimir(s)
            mensagem = chat_gpt

            print(f'usuário:{usuario}')
            print(f'ChatGPT:{chat_gpt}')

            entrada = input()
        entrada = input()

    if entrada == 'Qual era a tradução?':
        if mensagem == '':
            print(f'Não tem nada pra traduzir')
        else:
            descomprimida = descomprimir(mensagem)
            print(f'Descobri! É: {descomprimida}, tá de brincadeira né?')

    if entrada != 'Preciso parar de usar o ChatGPT':
        entrada = input()