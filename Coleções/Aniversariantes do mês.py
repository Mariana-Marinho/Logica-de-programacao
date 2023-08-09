def tem_aniversariante(dicionario, numero):
  ''' retorna uma lista de tuplas contendo o nome e especie dos animais aniversariantes '''
  animais = []
  for nome, dados in dicionario.items():
    if dados['mes'] == numero:
      animais.append((nome, dados['especie']))
  return animais


cadastro = dict()
quantidade = int(input())

for i in range(quantidade):
  entrada = input().split()
  mes = int(entrada[2].split('/')[1])
  cadastro[entrada[0]] = {'especie': entrada[1], 'mes': mes}

cadastro = dict(sorted(cadastro.items()))
m = int(input())
aniversariantes = (tem_aniversariante(cadastro, m))

if len(aniversariantes) > 0:
  print('E os donos da festa do mes sao:')
  for nome, especie in aniversariantes:
    print(f'{nome} - {especie}')
else:
  print('Sem festa esse mes. :(')
