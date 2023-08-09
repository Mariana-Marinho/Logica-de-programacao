Nome1 = input()
Nome2 = input()
Gol1 = Gol2 = 0

Entrada1 = input()
if Entrada1 == 'Gol':
    Gol1 += 1

Entrada2 = input()
if Entrada2 == 'Gol':
    Gol2 += 1

Entrada3 = input()
if Entrada3 == 'Gol':
    Gol1 += 1

Entrada4 = input()
if Entrada4 == 'Gol':
    Gol2 += 1

Entrada5 = input()
if Entrada5 == 'Gol':
    Gol1 += 1

Entrada6 = input()
if Entrada6 == 'Gol':
    Gol2 += 1

Entrada7 = input()
if Entrada7 == 'Gol':
    Gol1 += 1

if Gol1 - Gol2 > 2 or Gol2 - Gol1 >= 2:
    # se a diferença de gols for maior ou igual a 2 quando tiverem batido 7 pênaltis
    if Gol1 > Gol2:
        print(f'{Nome1} vence a disputa de pênaltis por {Gol1} a {Gol2} e avança de fase!')
    else:
        print(f'{Nome2} vence a disputa de pênaltis por {Gol2} a {Gol1} e avança de fase!')

else:
    Entrada8 = input()
    if Entrada8 == 'Gol':
        Gol2 += 1

    if Gol1 - Gol2 >= 2 or Gol2 - Gol1 >= 2:
        # se a diferença de gols for maior ou igual a 2 quando tiverem batido 8 pênaltis
        if Gol1 > Gol2:
            print(f'{Nome1} vence a disputa de pênaltis por {Gol1} a {Gol2} e avança de fase!')
        else:
            print(f'{Nome2} vence a disputa de pênaltis por {Gol2} a {Gol1} e avança de fase!')

    else:
        Entrada9 = input()
        if Entrada9 == 'Gol':
            Gol1 += 1

        if Gol1 - Gol2 >= 2 or Gol2 - Gol1 >= 1:
            # se a diferença de gols for maior ou igual a 2 quando tiverem batido 9 pênaltis
            if Gol1 > Gol2:
                print(f'{Nome1} vence a disputa de pênaltis por {Gol1} a {Gol2} e avança de fase!')
            else:
                print(f'{Nome2} vence a disputa de pênaltis por {Gol2} a {Gol1} e avança de fase!')

        else:
            Entrada10 = input()
            if Entrada10 == 'Gol':
                Gol2 += 1

            if Gol2 == Gol1:
                print(f'Ambas as seleções terminaram com {Gol1} gols, mas o desempate vai ficar para outro dia.')

            else:
                if Gol1 > Gol2:
                    print(f'{Nome1} vence a disputa de pênaltis por {Gol1} a {Gol2} e avança de fase!')
                else:
                    print(f'{Nome2} vence a disputa de pênaltis por {Gol2} a {Gol1} e avança de fase!')

