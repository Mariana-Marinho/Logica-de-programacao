Nome1 = input()
Bolas1 = int(input())
Finalizacoes1 = int(input())
Gols1 = int(input())

Nome2 = input()
Bolas2 = int(input())
Finalizacoes2 = int(input())
Gols2 = int(input())

Nome3 = input()
Bolas3 = int(input())
Finalizacoes3 = int(input())
Gols3 = int(input())

melhor_jogador = ''

# se os jogadores com maior nº de bolas estiverem empatados
if Bolas1 == Bolas2 and Bolas1 > Bolas3:
    print('Tite está mais indeciso do que nunca!')
    taxa2 = Gols2 * 100 / Finalizacoes2
    taxa1 = Gols1 * 100 / Finalizacoes1
    if taxa1 > taxa2:
        melhor_jogador = Nome1
        print(Nome1)
        print(Nome2)
        print(Nome3)
    else:
        melhor_jogador = Nome3
        print(Nome3)
        print(Nome1)
        print(Nome2)

elif Bolas1 == Bolas3 and Bolas1 > Bolas2:
    print('Tite está mais indeciso do que nunca!')
    taxa1 = Gols1 * 100 / Finalizacoes1
    taxa3 = Gols3 * 100 / Finalizacoes3
    if taxa1 > taxa3:
        melhor_jogador = Nome1
        print(Nome1)
        print(Nome3)
        print(Nome2)
    else:
        melhor_jogador = Nome3
        print(Nome3)
        print(Nome1)
        print(Nome2)
elif Bolas2 == Bolas3 and Bolas2 > Bolas1:
    print('Tite está mais indeciso do que nunca!')
    taxa2 = Gols2 * 100 / Finalizacoes2
    taxa3 = Gols3 * 100 / Finalizacoes3
    if taxa2 > taxa3:
        melhor_jogador = Nome2
        print(Nome2)
        print(Nome3)
        print(Nome1)
    else:
        melhor_jogador = Nome3
        print(Nome3)
        print(Nome2)
        print(Nome1)

elif Bolas1 == Bolas2 == Bolas3:
    print('Tite está mais indeciso do que nunca!')
    taxa1 = Gols1 * 100 / Finalizacoes1
    taxa2 = Gols2 * 100 / Finalizacoes2
    taxa3 = Gols3 * 100 / Finalizacoes3
    if taxa1 > taxa2:
        if taxa2 > taxa3:
            melhor_jogador = Nome1
            print(Nome1)
            print(Nome2)
            print(Nome3)
        elif taxa3 > taxa2:
            if taxa1 > taxa3:
                melhor_jogador = Nome1
                print(Nome1)
                print(Nome3)
                print(Nome2)
            if taxa3 > taxa1:
                melhor_jogador = Nome3
                print(Nome3)
                print(Nome1)
                print(Nome2)
    elif taxa2 > taxa1:
        if taxa1 > taxa3:
            melhor_jogador = Nome2
            print(Nome2)
            print(Nome1)
            print(Nome3)
        elif taxa3 > taxa1:
            if taxa2 > taxa3:
                melhor_jogador = Nome2
                print(Nome2)
                print(Nome3)
                print(Nome1)
            elif taxa3 > taxa2:
                melhor_jogador = Nome3
                print(Nome3)
                print(Nome2)
                print(Nome1)

if Bolas1 > Bolas2:
    if Bolas1 > Bolas3:
        print(Nome1)
        melhor_jogador = Nome1
        if Bolas2 > Bolas3:
            print(Nome2)
            print(Nome3)
        elif Bolas3 > Bolas2:
            print(Nome3)
            print(Nome2)
        else:
            taxa2 = Gols2 * 100 / Finalizacoes2
            taxa3 = Gols3 * 100 / Finalizacoes3
            if taxa2 > taxa3:
                print(taxa2)
                print(taxa3)
            else:
                print(taxa3)
                print(taxa2)

    elif Bolas3 > Bolas1:
        melhor_jogador = Nome3
        print(Nome3)
        print(Nome1)
        print(Nome2)

else:
    if Bolas2 > Bolas3:
        melhor_jogador = Nome2
        print(Nome2)

        if Bolas3 > Bolas1:
            print(Nome3)
            print(Nome1)
        elif Bolas1 > Bolas3:
            print(Nome1)
            print(Nome3)

        elif Bolas1 == Bolas3:
            taxa1 = Gols1 * 100 / Finalizacoes1
            taxa3 = Gols3 * 100 / Finalizacoes3
            if taxa1 > taxa3:
                print(Nome1)
                print(Nome3)
            else:
                print(Nome3)
                print(Nome1)
    elif Bolas2 < Bolas3:
        melhor_jogador = Nome3
        print(Nome3)
        if Bolas2 > Bolas1:
            print(Nome2)
            print(Nome1)
        elif Bolas1 == Bolas2:
            taxa1 = Gols1 * 100 / Finalizacoes1
            taxa2 = Gols2 * 100 / Finalizacoes2
            if taxa1 > taxa2:
                print(Nome1)
                print(Nome2)
            else:
                print(Nome2)
                print(Nome1)

print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')

if melhor_jogador == Nome1:
    if Bolas1 <= 10:
        print(f'{melhor_jogador}?! Sei não hein Galvão…')
    else:
        print(f'{melhor_jogador}! Dessa vez o hexa vem pra casa!!')
elif melhor_jogador == Nome2:
    if Bolas2 <= 10:
        print(f'{melhor_jogador}?! Sei não hein Galvão…')
    else:
        print(f'{melhor_jogador}! Dessa vez o hexa vem pra casa!!')
elif melhor_jogador == Nome3:
    if Bolas3 <= 10:
        print(f'{melhor_jogador}?! Sei não hein Galvão…')
    else:
        print(f'{melhor_jogador}! Dessa vez o hexa vem pra casa!!')