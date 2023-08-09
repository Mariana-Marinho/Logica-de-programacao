n = int(input())
soma = 0
melhor_lugar = pior_lugar = sugestoes = ''
empate = maior_nota = pior_nota = 0

for i in range(n):
    nome_lugar = input()

    while True:
        nota = int(input())

        if nota < 0:
            break

        soma += nota

    if i == 0:
        # primeiro lugar
        sugestoes = nome_lugar
        melhor_lugar = nome_lugar
        pior_lugar = nome_lugar
        maior_nota = soma
        pior_nota = soma

    else:
        if soma > maior_nota:
            empate = 0
            melhor_lugar = nome_lugar
            maior_nota = soma
            sugestoes = nome_lugar

        elif soma == maior_nota:
            sugestoes += ', ' + nome_lugar
            empate += 1

        if soma < pior_nota:
            pior_lugar = nome_lugar
            pior_nota = soma

    soma = 0

if empate != 0:
    print(sugestoes)
    print('Tantas opções')
else:
    print(f'{melhor_lugar} ganhou de lavada de {pior_lugar}, com {maior_nota} vs {pior_nota}')