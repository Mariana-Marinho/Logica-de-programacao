contador = 0
while True:
  frase = input()
  if frase == 'O relógio descarregou!' :
    print(f'Corra Ben! Você já derrotou {contador} aliens')
    break
  elif frase == 'Por hoje já deu':
    print(f'Muito Ben Ben! hehe você derrotou {contador} aliens hoje')
    break
  contador += 1
