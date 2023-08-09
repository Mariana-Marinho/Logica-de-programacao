def reverter(frase, pos=0):
  if len(frase)-1 == pos:
    return frase[pos]
  else:
    # tira o primeiro elemento da frase e o reposiciona no fim
    return reverter(frase, pos+1) + frase[pos]

entrada = input()
print(reverter(entrada))
