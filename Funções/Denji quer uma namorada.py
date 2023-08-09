def ler_nome(n):
    # checa se o nome não é maior que 7 e não retorna nenhum valor
    if len(n) > 7:
        return False
    else:
        return True


def preencher_lista(n, prob, lista):
    # preenche a lista com o nome seguido da probabilidade e retorna a lista
    if nome != 'Makima':
        lista.append(n)
        lista.append(prob)
    return lista


def checar_relacionamentos(boas, ruins):
    # imprime as frases conforme as condicoes dos possiveis relacionamentos
    if len(boas) > len(ruins):
        print('Epa ai sim! E hoje pochita!!')

        if len(ruins) == 0:
            for i in range(0, len(boas), 2):
                print(f'nome: {boas[i]} - chances de morrer: {boas[i + 1]}%')

    else:
        print('Desculpa pochita acho que nao vai ser hoje que voce vai poder ver meus sonhos')


pretendentes = []
assassinas = []

nome = input()
while nome != 'cabo':

    if ler_nome(nome):
        if nome == 'Makima':
            print('Woof Woof')
        probabilibade = int(input())

        if probabilibade <= 50 or nome == 'Makima':
            print(f'Beleza {nome}!! Essa é uma boa pretendente!')
            pretendentes = preencher_lista(n=nome, prob=probabilibade, lista=pretendentes)

        else:
            print(
                f'{nome}, mais uma que so quer o coraçao do chainsaw man, quando que alguem vai querer o meu coraçao!?!?')
            assassinas = preencher_lista(n=nome, prob=probabilibade, lista=assassinas)

    else:
        print(f'Er {nome[0:2]}.. errr... nao consigo lembrar, melhor deixar para la')

    nome = input()

checar_relacionamentos(pretendentes, assassinas)
