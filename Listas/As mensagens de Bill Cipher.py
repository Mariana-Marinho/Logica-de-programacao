alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a']
palavra = str()
mensagem = list()
soma_pares = soma_impares = 0
produto = 1

n = int(input())

for i in range(n):
    espaco = input()
    palavra_decodificada = input()
    espaco = input()
    palavra_codificada = input()

    if palavra_decodificada == 'Portal':

        for caractere in palavra_codificada:

            if caractere in alfabeto:
                indice_letra_codificada = alfabeto.index(caractere)
                letra_mensagem = alfabeto[indice_letra_codificada + 1]
                palavra += letra_mensagem

        if palavra != '':
            mensagem.append(palavra)

        palavra = ''

    elif palavra_decodificada == 'Experimento':

        for caractere in palavra_codificada:

            if caractere in '0123456789' and int(caractere) % 2 == 0:
                soma_pares += int(caractere)

        mensagem.append(soma_pares)

    elif palavra_decodificada == 'Realidade':

        for caractere in palavra_codificada:

            if caractere in '0123456789' and int(caractere) % 2 != 0:
                soma_impares += int(caractere)

        mensagem.append(soma_impares)

    else:
        # palavra_decodificada == 'Schembulock':

        for caractere in palavra_codificada:

            if caractere in '0123456789':
                produto *= int(caractere)

        mensagem.append(produto)

if len(mensagem) == 0:
    print(f'Esse formato de mensagem nem Bill Cipher entenderia!')

else:
    print(f'Consegui! A mensagem decodificada de Bill Cipher é:', end='')
    for palavra in mensagem:
        print(f' {palavra}', end='')
