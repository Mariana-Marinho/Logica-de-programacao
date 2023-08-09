n = int(input())
diarios = list()

for i in range(n):
    entrada = input()

    # onde está a vírgula
    index_virgula = entrada.index(",")

    # o conteudo vai até a vírgula
    conteudo = entrada[0:index_virgula]

    numero_do_diario = int(entrada[-1])

    diarios.append(conteudo)
    diarios.append(numero_do_diario)

m = int(input())

for i in range(m):
    conteudo_buscado = input()

    if conteudo_buscado in diarios:
        index_conteudo = diarios.index(conteudo_buscado)
        numero_do_diario = diarios[index_conteudo + 1]
        print(f"Informacoes sobre {conteudo_buscado} estao no Diario {numero_do_diario}")

    else:
        print(f"Nenhum dos diarios possui informacoes sobre {conteudo_buscado}")
