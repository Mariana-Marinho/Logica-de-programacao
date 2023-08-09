nome_jogador = str(input())

if nome_jogador == 'Alisson' or nome_jogador == 'Ederson' or nome_jogador == 'Weverton':
    print(f'{nome_jogador} foi convocado e jogará como goleiro!')

elif nome_jogador == 'Daniel Alves' or nome_jogador == 'Danilo' or nome_jogador == 'Alex Sandro' or nome_jogador == 'Alex Telles':
    print(f'{nome_jogador} foi convocado e jogará como lateral!')

elif nome_jogador == 'Marquinhos' or nome_jogador == 'Thiago Silva' or nome_jogador == 'Éder Militão' or nome_jogador == 'Bremer':
    print(f'{nome_jogador} foi convocado e jogará como zagueiro!')

elif nome_jogador == 'Casemiro' or nome_jogador == 'Fabinho' or nome_jogador == 'Fred' or nome_jogador == 'Bruno Guimarães' or nome_jogador == 'Lucas Paquetá' or nome_jogador == 'Everton Ribeiro':
    print(f'{nome_jogador} foi convocado e jogará como meia!')

elif nome_jogador == 'Neymar' or nome_jogador == 'Raphinha' or nome_jogador == 'Vini Jr.' or nome_jogador == 'Antony' or nome_jogador == 'Richarlison' or nome_jogador == 'Rodrygo' or nome_jogador == 'Pedro' or nome_jogador == 'Gabriel Jesus' or nome_jogador == 'Gabriel Martinelli':
    print(f'{nome_jogador} foi convocado e jogará como atacante!')

else:
    print(f'{nome_jogador} não foi convocado, mas quem sabe na próxima?')
