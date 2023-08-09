def prog_aritmetica(primeiro, razao, posicao):
  if posicao == 1:
    return primeiro
  else:
    return prog_aritmetica(primeiro, razao, posicao-1) + razao


# separar os numeros da string em 3 variaveis
entrada = input().split()
num_1 = int(entrada[0])
num_2 = int(entrada[1])
num_3 = int(entrada[2])

n = int(input())

r = num_2 - num_1
numero = prog_aritmetica(num_1, r, n)
print(f'Na progressão aritmética cujos três primeiros números são {num_1}, {num_2} e {num_3}, o {n}º elemento é {numero} e a razão da progressão é {r}.')
