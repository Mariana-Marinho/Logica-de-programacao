FavoritismoBr = int(input())
NomeOponente1 = input()
FavoritismoOponente1 = int(input())
GolsBR1 = int(input())
GolsOPO1 = int(input())

if (GolsBR1 > GolsOPO1) or (GolsBR1 == GolsOPO1 and FavoritismoBr > FavoritismoOponente1):
    if GolsBR1 > GolsOPO1:
        print('Quem é que segura o Brasil???')
    else:
        print('No sufoco, o Brasil conseguiu ganhar!!!')

    if GolsBR1 - GolsOPO1 == 1:
        FavoritismoBr += 10
    elif GolsBR1 - GolsOPO1 == 2:
        FavoritismoBr += 20
    elif GolsBR1 - GolsOPO1 >= 3:
        FavoritismoBr += 30

    NomeOponente2 = input()
    FavoritismoOponente2 = int(input())
    GolsBR2 = int(input())
    GolsOPO2 = int(input())

    if (GolsBR2 > GolsOPO2) or (GolsBR2 == GolsOPO2 and FavoritismoBr > FavoritismoOponente2):
        if GolsBR2 > GolsOPO2:
            print('Quem é que segura o Brasil???')
        else:
            print('No sufoco, o Brasil conseguiu ganhar!!!')

        if GolsBR2 - GolsOPO2 == 1:
            FavoritismoBr += 10
        elif GolsBR2 - GolsOPO2 == 2:
            FavoritismoBr += 20
        elif GolsBR2 - GolsOPO2 >= 3:
            FavoritismoBr += 30

        NomeOponente3 = input()
        FavoritismoOponente3 = int(input())
        GolsBR3 = int(input())
        GolsOPO3 = int(input())

        if (GolsBR3 > GolsOPO3) or (GolsBR3 == GolsOPO3 and FavoritismoBr > FavoritismoOponente3):
            if GolsBR3 > GolsOPO3:
                print('Quem é que segura o Brasil???')
            else:
                print('No sufoco, o Brasil conseguiu ganhar!!!')

            if GolsBR3 - GolsOPO3 == 1:
                FavoritismoBr += 10
            elif GolsBR3 - GolsOPO3 == 2:
                FavoritismoBr += 20
            elif GolsBR3 - GolsOPO3 >= 3:
                FavoritismoBr += 30

            NomeOponente = input()
            FavoritismoOponente = int(input())

            if FavoritismoBr >= FavoritismoOponente:
                print('O BRASIL VAI SER HEXAAAAAAAA')
            else:
                print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {NomeOponente} na simulação')

        else:
            if GolsBR3 < GolsOPO3:
                print(f'Infelizmente essa seleção dx {NomeOponente3} era muito forte para o Brasil.')
            else:
                print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')

    else:
        if GolsBR2 < GolsOPO2:
            print(f'Infelizmente essa seleção dx {NomeOponente2} era muito forte para o Brasil.')
        else:
            print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')


else:
    if GolsBR1 < GolsOPO1:
        print(f'Infelizmente essa seleção dx {NomeOponente1} era muito forte para o Brasil.')
    else:
        print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
