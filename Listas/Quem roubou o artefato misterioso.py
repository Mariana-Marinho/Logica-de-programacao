suspeitos = []

entrada = input()

while entrada != "ja temos nossa lista de suspeitos":

    if entrada == "novo suspeito - altissima periculosidade":
        nome = input()
        suspeitos.insert(0, nome)

    elif entrada == "novo suspeito - pouco perigoso":
        nome = input()
        suspeitos.append(nome)

    elif entrada == "livre de suspeita, pode remover":
        nome = input()
        suspeitos.remove(nome)

    elif entrada == "sujeito mais perigoso do que pensavamos":
        indice_atual = int(input())
        indice_novo = int(input())

        # trocar a posicao
        suspeitos[indice_atual], suspeitos[indice_novo] = suspeitos[indice_novo], suspeitos[indice_atual]

    elif entrada == "que estranho, esses dois meliantes… troque-os de lugar":
        nome_1 = input()
        nome_2 = input()

        indice_1 = suspeitos.index(nome_1)
        indice_2 = suspeitos.index(nome_2)

        # trocar a posição
        suspeitos[indice_1], suspeitos[indice_2] = suspeitos[indice_2], suspeitos[indice_1]

    elif entrada == "essa posicao nao esta de acordo, ele nao e tao perigoso assim":
        nome = input()
        suspeitos.remove(nome)
        suspeitos.append(nome)

    else:
        # entrada == "como a lista esta ficando?"
        for sus in suspeitos:

            # printar com um espaço no meio
            if suspeitos.index(sus) == 0:
                print(sus, end='')
            else:
                print(f' {sus}', end='')

        print()

    entrada = input()

print("O resultado final ficou assim:")

for sus in suspeitos:

    if suspeitos.index(sus) == 0:
        print(sus, end='')
    else:
        print(f' {sus}', end='')

print()