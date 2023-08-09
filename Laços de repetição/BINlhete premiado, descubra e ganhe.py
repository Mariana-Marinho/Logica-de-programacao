n_binario = int(input())
palpite_01 = int(input())

chances = 3
i = n_decimal = 0
acertou = ''
while n_binario != 0:
  # binario para decimal
  resto = n_binario % 10
  n_decimal += (resto * (2 ** i))
  i += 1
  n_binario = int(n_binario / 10)

if palpite_01 != n_decimal:
  chances -= 1
  print(f'Resposta incorreta. Mas não desista! Você ainda tem {chances} chance(s).')
  palpite_02 = int(input())
  if palpite_02 != n_decimal:
    chances -= 1
    print(f'Resposta incorreta. Mas não desista! Você ainda tem {chances} chance(s).')
    palpite_03 = int(input())
    if palpite_03 != n_decimal:
      acertou = 'nao'
    else:
      acertou = 'sim'
  else:
    acertou = 'sim'
else:
  acertou = 'sim'

if acertou == 'sim':
  print('Parabéns!! Você acertou!')
  if n_decimal == 1:
    print('Férias inesquecíveis estão te esperando!')
    print('Seu destino será Porto de Galinhas (BRA).')
    print('Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!')

  elif n_decimal == 2:
    print('Férias inesquecíveis estão te esperando!')
    print('Seu destino será Fernando de Noronha (BRA).')
    print('Belíssimas praias estão por vir.')
    print('Não esqueça o protetor solar.')

  elif n_decimal == 3:
    print('Férias inesquecíveis estão te esperando!')
    print('Seu destino será Gramado (BRA).')
    print('Aproveite passeios e paisagens espetaculares no sul do país!')

  elif n_decimal == 4:
    print('Férias inesquecíveis estão te esperando!')
    print('Seu destino será Berlim (ALE).')
    print('Desfrute de muita cultura e de experiências incríveis!')
    print('Prepare os casacos de frio!')

  elif n_decimal == 5:
    print('Férias inesquecíveis estão te esperando!')
    print('Seu destino será Tóquio (JPN).')
    print('Viva uma experiência inesquecível explorando um país do outro lado do mundo.')
    print('Prepare-se para muitas horas de voo!')

  else:
    print('Mas, infelizmente, hoje não é o seu dia de sorte.')
    print('Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.')
    print('Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')

else:
  # se errou o palpite
  if n_decimal in range(1, 6):
    # se o bilhete for premiado
    print('Infelizmente mais uma resposta incorreta.')
    print('Agradecemos sua participação!')
    print('Seu bilhete era premiado. Que pena!')
  else:
    # se o bilhete não for premiado
    print('Infelizmente mais uma resposta incorreta.')
    print('Agradecemos sua participação!')
    print('Pelo menos seu bilhete não era premiado.')
    print('Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')
