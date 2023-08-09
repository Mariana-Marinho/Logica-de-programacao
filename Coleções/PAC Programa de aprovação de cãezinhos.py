def boletim(dicionario):
    """ retorna 3 listas que contêm os dados de cada animal de acordo com sua situação """
    aprovados = []
    reprovados = []
    recuperacao = []

    for nome, dados in dicionario.items():
        nota = (float(dados[1]) + float(dados[2]) + float(dados[3])) / 3

        if nota >= 3:
            aprovados.append((nome, dados[0], nota))
        elif nota < 2:
            reprovados.append((nome, dados[0], nota))
        else:
            recuperacao.append((nome, dados[0], nota))

    return aprovados, reprovados, recuperacao


m = int(input())
animais = dict()

for i in range(m):
    # preencher dicionario com o nome de cada animal e seus dados
    entrada = input().split(',')
    animais[entrada[0]] = tuple(entrada[1:])

# cada lista recebe o nome e dados de acordo com a situação do dog
aprov, reprov, recup = boletim(animais)

if len(aprov) > 0:
    print('Estao aprovados e de parabens os seguintes coleguinhas:')
    for dado in aprov:
        print(f'{dado[0]} -{dado[1]} - media: {dado[2]:.2f}')
if len(reprov) > 0:
    print('Os colegas a seguir nao se comportaram bem e precisam de ajuda profissional (entrar em contato urgente):')
    for dado in reprov:
        print(f'{dado[0]} -{dado[1]} - media: {dado[2]:.2f}')
if len(recup) > 0:
    print('Esses queridos terao uma nova chance e prometem melhorar:')
    for dado in recup:
        print(f'{dado[0]} -{dado[1]} - media: {dado[2]:.2f}')
